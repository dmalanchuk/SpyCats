from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

from src.repositories.cats_repo import CatRepository
from src.services.cats_service import CatService

async def get_cat_repository(
    session: AsyncSession = Depends(get_session)
) -> CatRepository:
    return CatRepository(session)

async def get_cat_service(
    repo: CatRepository = Depends(get_cat_repository)
) -> CatService:
    return CatService(repo)