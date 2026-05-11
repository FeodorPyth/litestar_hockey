from advanced_alchemy import service

from db.models import CityDB
from db.repositories import CityRepository


class CityService(service.SQLAlchemyAsyncRepositoryService[CityDB]):
    repository_type = CityRepository
    # check this
    match_fields = ["name"]
