from sqlalchemy.ext.asyncio import AsyncSession

from src.models.cats_model import MissionsModel, TargetsModel
from src.schemas.missions_schema import MissionCreate

class MissionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session