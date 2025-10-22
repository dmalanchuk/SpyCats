from fastapi import APIRouter, Depends, status
from src.services.cats_service import CatService
from src.dependencies import get_cat_service

from src.schemas.cats_schema import CatCreate, CatResponse, CatUpdate

router = APIRouter(prefix="/cats")


@router.post(
    "/",
    response_model=CatResponse,
    summary="Create new spy cats",
    description="This endpoint allows you to create a new cpy cats",
    status_code=201,
    responses={
        status.HTTP_201_CREATED: {"description": "The spy cat was successfully created."},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid breed provided."},
        status.HTTP_409_CONFLICT: {"description": "A cat with this name already exists."},
        status.HTTP_503_SERVICE_UNAVAILABLE: {"description": "TheCatAPI is currently unavailable."},
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
    summary="Get all Spy Cats",
    responses={
        status.HTTP_200_OK: {"description": "Successfully retrieved the list of all spy cats."}
    },

)
async def get_all_spy_cats(
        cat_service: CatService = Depends(get_cat_service)
):
    return await cat_service.get_all_cats()


@router.get(
    "/{cat_id}",
    response_model=CatResponse,
    summary="Get a single Spy Cat",
    responses={
        status.HTTP_200_OK: {"description": "Successfully retrieved the spy cat."},
        status.HTTP_404_NOT_FOUND: {"description": "A cat with the specified ID was not found."},
    },
)
async def get_spy_cat(
        cat_id: int,
        cat_service: CatService = Depends(get_cat_service)
):
    return await cat_service.get_cat_by_id(cat_id)


@router.patch(
    "/{cat_id}",
    response_model=CatResponse,
    summary="Update a Cat's salary",
    responses={
        status.HTTP_200_OK: {"description": "The cat's salary was successfully updated."},
        status.HTTP_404_NOT_FOUND: {"description": "A cat with the specified ID was not found."},
    },
)
async def update_cat_salary(
        cat_id: int,
        salary_data: CatUpdate,
        cat_service: CatService = Depends(get_cat_service)
):
    return await cat_service.update_cat_salary(cat_id, salary_data.salary)


@router.delete(
    "/{cat_id}",
    status_code=204,
    summary="Delete a Spy Cat",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "The cat was successfully deleted."},
        status.HTTP_400_BAD_REQUEST: {"description": "Cannot delete a cat that is currently on a mission."},
        status.HTTP_404_NOT_FOUND: {"description": "A cat with the specified ID was not found."},
    },
)
async def delete_spy_cat(
        cat_id: int,
        cat_service: CatService = Depends(get_cat_service)
):
    await cat_service.remove_cat(cat_id)
    return None
