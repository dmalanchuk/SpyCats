from fastapi import APIRouter, Depends, status
from src.services.missions_service import MissionService
from src.schemas.missions_schema import MissionCreate, MissionResponse
from src.dependencies import get_mission_service

router = APIRouter(prefix="/missions")


@router.post(
    "/",
    response_model=MissionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new Mission with its Targets",
    responses={
        status.HTTP_201_CREATED: {"description": "Mission created successfully."},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid data provided (e.g., duplicate target names)."},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"description": "Validation error (e.g., more than 3 targets)."}
    },
)
async def create_mission_with_targets(
        mission_data: MissionCreate,
        mission_service: MissionService = Depends(get_mission_service)
):
    new_mission = await mission_service.create_new_mission(mission_data)
    return new_mission