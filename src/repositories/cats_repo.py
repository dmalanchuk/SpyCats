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

    async def get_all_cats(self) -> list[CatsModel]:
        stmt = select(CatsModel).order_by(CatsModel.id)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_cat_by_id(self, cat_id: int) -> Optional[CatsModel]:
        return await self.session.get(CatsModel, cat_id)

    async def update_cat(self, cat: CatsModel) -> CatsModel:
        await self.session.commit()
        await self.session.refresh(cat)
        return cat

    async def delete_cat(self, cat: CatsModel) -> None:
        await self.session.delete(cat)
        await self.session.commit()
