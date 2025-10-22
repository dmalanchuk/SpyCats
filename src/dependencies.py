from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

from src.repositories.cats_repo import CatRepository
from src.services.cats_service import CatService
from src.repositories.missions_repo import MissionRepository
from src.services.missions_service import MissionService
from src.repositories.targets_repo import TargetRepository
from src.services.targets_service import TargetService


async def get_cat_repository(
        session: AsyncSession = Depends(get_session)
) -> CatRepository:
    return CatRepository(session)


async def get_cat_service(
        repo: CatRepository = Depends(get_cat_repository)
) -> CatService:
    return CatService(repo)


async def get_mission_repository(
        session: AsyncSession = Depends(get_session)
) -> MissionRepository:
    return MissionRepository(session)


async def get_mission_service(
        mission_repo: MissionRepository = Depends(get_mission_repository),
        cat_repo: CatRepository = Depends(get_cat_repository)
) -> MissionService:
    return MissionService(mission_repo=mission_repo, cat_repo=cat_repo)


async def get_target_repository(
        session: AsyncSession = Depends(get_session)
) -> TargetRepository:
    return TargetRepository(session)


async def get_target_service(
        repo: TargetRepository = Depends(get_target_repository)
) -> TargetService:
    return TargetService(repo)
