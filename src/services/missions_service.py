from fastapi import HTTPException, status

from src.repositories.missions_repo import MissionRepository
from src.repositories.cats_repo import CatRepository
from src.schemas.missions_schema import MissionCreate
from src.models.cats_model import MissionsModel


class MissionService:
    def __init__(self, mission_repo: MissionRepository, cat_repo: CatRepository):
        self.mission_repo = mission_repo
        self.cat_repo = cat_repo

    # create new mission
    async def create_new_mission(self, mission_data: MissionCreate) -> MissionsModel:
        target_names = [target.name for target in mission_data.targets]
        if len(target_names) != len(set(target_names)):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Target names within a single mission must be unique."
            )
        new_mission = await self.mission_repo.create_mission(mission_data)
        return new_mission

    # assign cat to mission
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

    # delete mission
    async def remove_mission(self, mission_id: int) -> None:
        mission = await self.mission_repo.get_mission_by_id(mission_id)
        if not mission:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Mission {mission_id} not found.")

        if mission.cat is not None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "Cannot delete a mission that has a cat assigned.")

        await self.mission_repo.delete_mission(mission)

    # get all missions
    async def get_all_missions(self) -> list[MissionsModel]:
        return await self.mission_repo.get_all_missions()

    async def get_mission_by_id(self, mission_id: int) -> MissionsModel:
        mission = await self.mission_repo.get_mission_by_id(mission_id)
        if not mission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Mission with id {mission_id} not found."
            )
        return mission
