from fastapi import HTTPException, status

from src.repositories.missions_repo import MissionRepository
from src.schemas.missions_schema import MissionCreate
from src.models.cats_model import MissionsModel


class MissionService:
    def __init__(self, mission_repo: MissionRepository):
        self.mission_repo = mission_repo

    async def create_new_mission(self, mission_data: MissionCreate) -> MissionsModel:
        target_names = [target.name for target in mission_data.targets]
        if len(target_names) != len(set(target_names)):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Target names within a single mission must be unique."
            )

        new_mission = await self.mission_repo.create_mission(mission_data)
        return new_mission
