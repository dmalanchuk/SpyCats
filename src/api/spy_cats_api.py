from fastapi import APIRouter, Depends
from src.schemas.cats_schema import CatCreate, CatResponse
from src.services.cats_service import CatService
from src.dependencies import get_cat_service

router = APIRouter(prefix="/cats")


@router.post(
    "/",
    response_model=CatResponse,
    summary="Create new spy cats",
    description="This endpoint allows you to create a new cpy cats",
    status_code=201,
    responses={
        201: {"description": "cats created successfully"},
        400: {"description": "Invalid request"},
    },
)
async def create_spy_cats(
        cat_data: CatCreate,
        cat_service: CatService = Depends(get_cat_service)
):
    return await cat_service.create_new_cat(cat_data)


@router.get(
    "/",
    response_model=list[CatResponse],
    summary="Get all Spy Cats"
)
async def get_all_spy_cats(
    cat_service: CatService = Depends(get_cat_service)
):
    return await cat_service.get_all_cats()

@router.get(
    "/{cat_id}",
    response_model=CatResponse,
    summary="Get a single Spy Cat"
)
async def get_spy_cat(
    cat_id: int,
    cat_service: CatService = Depends(get_cat_service)
):
    return await cat_service.get_cat_by_id(cat_id)