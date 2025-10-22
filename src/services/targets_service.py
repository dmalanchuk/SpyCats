from fastapi import HTTPException, status
from src.repositories.targets_repo import TargetRepository
from src.schemas.targets_schema import TargetStatus
from src.models.database_model import TargetsModel


class TargetService:
    def __init__(self, repo: TargetRepository):
        self.repo = repo

    # update target notes and status
    async def _get_target_and_check_frozen(self, target_id: int) -> TargetsModel:
        target = await self.repo.get_target_by_id(target_id)
        if not target:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Target {target_id} not found.")

        if target.mission.is_complete or target.status == "Completed":
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Cannot update notes or status for a completed target or mission."
            )
        return target

    # update target notes
    async def update_target_notes(self, target_id: int, notes: str) -> TargetsModel:
        target = await self._get_target_and_check_frozen(target_id)
        target.notes = notes
        return await self.repo.update_target(target)

    # update target status
    async def update_target_status(self, target_id: int, new_status: TargetStatus) -> TargetsModel:
        target = await self._get_target_and_check_frozen(target_id)
        target.status = new_status

        all_targets = target.mission.targets
        is_all_completed = all(t.status == "Completed" for t in all_targets)

        if is_all_completed:
            target.mission.is_complete = True

        return await self.repo.update_target(target)