from advanced_alchemy import service

from db.models import StadiumDB
from db.repositories import StadiumRepository


class StadiumService(service.SQLAlchemyAsyncRepositoryService[StadiumDB]):
    repository_type = StadiumRepository
    # check this
    match_fields = ["name"]
