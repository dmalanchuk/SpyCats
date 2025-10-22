import httpx
from fastapi import HTTPException, status

from src.repositories.cats_repositories import CatRepository
from src.schemas.cats_schema import CatCreate
from src.models.cats_model import CatsModel


class CatService:
    def __init__(self, cat_repo: CatRepository):
        self.cat_repo = cat_repo

    async def _validate_breed_from_api(self, breed_name: str) -> bool:
        api_url = f"https://api.thecatapi.com/v1/breeds/search?q={breed_name}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(api_url)
                response.raise_for_status()
                data = response.json()
                return any(breed['name'].lower() == breed_name.lower() for breed in data)
            except httpx.RequestError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Could not connect to TheCatAPI to validate breed."
                )

    async def create_new_cat(self, cat_data: CatCreate) -> CatsModel:

        existing_cat = await self.cat_repo.get_cat_by_name(cat_data.name)
        if existing_cat:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"A cat with name '{cat_data.name}' already exists."
            )

        is_breed_valid = await self._validate_breed_from_api(cat_data.breed)
        if not is_breed_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Breed '{cat_data.breed}' is not a valid cat breed."
            )

        new_cat = await self.cat_repo.create_cat(cat_data)
        return new_cat

    async def get_all_cats(self) -> list[CatsModel]:
        return await self.cat_repo.get_all_cats()

    async def get_cat_by_id(self, cat_id: int) -> CatsModel:
        cat = await self.cat_repo.get_cat_by_id(cat_id)
        if not cat:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cat with id {cat_id} not found."
            )
        return cat
