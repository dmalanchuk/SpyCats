from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from src.models.cats_model import CatsModel
from src.schemas.cats_schema import CatCreate


class CatRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_cat_by_name(self, name: str) -> Optional[CatsModel]:
        stmt = select(CatsModel).where(CatsModel.name == name)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create_cat(self, cat_data: CatCreate) -> CatsModel:
        new_cat = CatsModel(**cat_data.model_dump())

        self.session.add(new_cat)
        await self.session.commit()
        await self.session.refresh(new_cat)

        return new_cat
