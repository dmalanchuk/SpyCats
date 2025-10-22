from fastapi import Request

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

router = APIRouter(prefix="/spy")

@router.post(
    "/cats",
    summary="Create new spy cats",
    description="This endpoint allows you to create a new cpy cats",
    status_code=201,
    responses={
        201: {"description": "cats created successfully"},
        400: {"description": "Invalid request"},
    },
)
async def create_spy_cats(
        session: AsyncSession = Depends(get_session)
):
    return "hi"
