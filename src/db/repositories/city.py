from advanced_alchemy import repository

from db.models import CityDB


class CityRepository(repository.SQLAlchemyAsyncRepository[CityDB]):
    model_type = CityDB
