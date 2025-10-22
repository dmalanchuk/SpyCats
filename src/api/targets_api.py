from fastapi import APIRouter, Depends, status
from src.schemas.targets_schema import TargetResponse, TargetUpdateNotes, TargetUpdateStatus

from src.services.targets_service import TargetService
from src.dependencies import get_target_service

router = APIRouter(prefix="/targets")


@router.patch(
    "/{target_id}/notes",
    response_model=TargetResponse,
    summary="Update target's notes",
    responses={
        status.HTTP_200_OK: {"description": "Notes updated successfully."},
        status.HTTP_404_NOT_FOUND: {"description": "Target not found."},
        status.HTTP_400_BAD_REQUEST: {"description": "Target or mission is completed and cannot be changed."},
    },
)
async def update_notes(
        target_id: int,
        data: TargetUpdateNotes,
        service: TargetService = Depends(get_target_service)
):
    return await service.update_target_notes(target_id, data.notes)


@router.patch(
    "/{target_id}/status",
    response_model=TargetResponse,
    summary="Update target's status",
    responses={
        status.HTTP_200_OK: {"description": "Status updated successfully."},
        status.HTTP_404_NOT_FOUND: {"description": "Target not found."},
        status.HTTP_400_BAD_REQUEST: {"description": "Target or mission is completed and cannot be changed."},
    },
)
async def update_status(
        target_id: int,
        data: TargetUpdateStatus,
        service: TargetService = Depends(get_target_service)
):
    return await service.update_target_status(target_id, data.status)
