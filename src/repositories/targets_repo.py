from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select

from src.models.cats_model import TargetsModel, MissionsModel

class TargetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    # get target by id
    async def get_target_by_id(self, target_id: int) -> TargetsModel | None:
        stmt = (
            select(TargetsModel)
            .where(TargetsModel.id == target_id)
            .options(
                selectinload(TargetsModel.mission)
                .selectinload(MissionsModel.targets)
            )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    # update target notes
    async def update_target(self, target: TargetsModel) -> TargetsModel:
        await self.session.commit()
        await self.session.refresh(target)
        return target