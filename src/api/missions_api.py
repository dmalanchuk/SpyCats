from fastapi import APIRouter, Depends, status
from src.services.missions_service import MissionService
from src.schemas.missions_schema import MissionCreate, MissionResponse, MissionAssignCat
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


@router.patch(
    "/{mission_id}/assign-cat",
    response_model=MissionResponse,
    summary="Assign a cat to a mission",
    responses={
        status.HTTP_200_OK: {"description": "Cat successfully assigned."},
        status.HTTP_404_NOT_FOUND: {"description": "Mission or Cat not found."},
        status.HTTP_400_BAD_REQUEST: {"description": "Mission or Cat is not available."},
    },
)
async def assign_cat(
        mission_id: int,
        assignment_data: MissionAssignCat,
        mission_service: MissionService = Depends(get_mission_service)
):
    return await mission_service.assign_cat_to_mission(
        mission_id=mission_id,
        cat_id=assignment_data.cat_id
    )


@router.delete(
    "/{mission_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a mission",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Mission successfully deleted."},
        status.HTTP_404_NOT_FOUND: {"description": "Mission not found."},
        status.HTTP_400_BAD_REQUEST: {"description": "Mission has a cat assigned and cannot be deleted."},
    },
)
async def delete_mission(
        mission_id: int,
        mission_service: MissionService = Depends(get_mission_service)
):
    await mission_service.remove_mission(mission_id)
    return None
