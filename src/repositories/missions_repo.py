from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select

from src.models.cats_model import MissionsModel, TargetsModel
from src.schemas.missions_schema import MissionCreate


class MissionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_mission(self, mission_data: MissionCreate) -> MissionsModel:
        new_mission = MissionsModel(is_complete=False)

        targets = [
            TargetsModel(**target.model_dump(), mission=new_mission)
            for target in mission_data.targets
        ]

        self.session.add(new_mission)
        await self.session.commit()

        stmt = (
            select(MissionsModel)
            .where(MissionsModel.id == new_mission.id)
            .options(selectinload(MissionsModel.targets))
        )

        result = await self.session.execute(stmt)
        created_mission_with_targets = result.scalar_one()

        return created_mission_with_targets

    async def get_mission_by_id(self, mission_id: int) -> MissionsModel | None:
        stmt = (
            select(MissionsModel)
            .where(MissionsModel.id == mission_id)
            .options(
                selectinload(MissionsModel.targets),
                selectinload(MissionsModel.cat)
            )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_mission(self, mission: MissionsModel) -> MissionsModel:
        await self.session.commit()
        await self.session.refresh(mission)
        return mission

    async def delete_mission(self, mission: MissionsModel) -> None:
        await self.session.delete(mission)
        await self.session.commit()

    async def get_all_missions(self) -> list[MissionsModel]:
        stmt = (
            select(MissionsModel)
            .options(
                selectinload(MissionsModel.targets),
                selectinload(MissionsModel.cat)
            )
            .order_by(MissionsModel.id)
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
