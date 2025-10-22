from fastapi import HTTPException, status

from src.repositories.missions_repo import MissionRepository
from src.repositories.cats_repo import CatRepository
from src.schemas.missions_schema import MissionCreate
from src.models.cats_model import MissionsModel


class MissionService:
    def __init__(self, mission_repo: MissionRepository, cat_repo: CatRepository):
        self.mission_repo = mission_repo
        self.cat_repo = cat_repo

    async def assign_cat_to_mission(self, mission_id: int, cat_id: int) -> MissionsModel:
        mission = await self.mission_repo.get_mission_by_id(mission_id)
        if not mission:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Mission {mission_id} not found.")

        if mission.cat is not None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "This mission already has a cat assigned.")

        cat = await self.cat_repo.get_cat_by_id(cat_id)
        if not cat:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Cat {cat_id} not found.")

        if cat.mission_id is not None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Cat {cat_id} is already on another mission.")

        mission.cat = cat

        updated_mission = await self.mission_repo.update_mission(mission)
        return await self.mission_repo.get_mission_by_id(updated_mission.id)

    async def remove_mission(self, mission_id: int) -> None:
        mission = await self.mission_repo.get_mission_by_id(mission_id)
        if not mission:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Mission {mission_id} not found.")

        if mission.cat is not None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Cannot delete a mission that has a cat assigned.")

        await self.mission_repo.delete_mission(mission)
