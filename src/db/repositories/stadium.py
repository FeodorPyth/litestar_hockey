from advanced_alchemy import repository

from db.models import StadiumDB


class StadiumRepository(repository.SQLAlchemyAsyncRepository[StadiumDB]):
    model_type = StadiumDB
