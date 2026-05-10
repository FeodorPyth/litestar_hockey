from __future__ import annotations
from typing import TYPE_CHECKING, Annotated
from uuid import UUID

from litestar import Controller, get, post, put, delete
from litestar.params import Dependency, Parameter
from sqlalchemy.orm import selectinload

from db.models import CityDB
from domain.models import City, CityCreate, CityUpdate
from domain.services import CityService
from lib.deps import create_service_dependencies

if TYPE_CHECKING:
    from advanced_alchemy.filters import FilterTypes
    from advanced_alchemy.service.pagination import OffsetPagination


class CityController(Controller):
    tags = ["Cities"]
    path = "/cities"
    dependencies = create_service_dependencies(
        CityService,
        key="cities_service",
        load=[selectinload(CityDB.stadiums), selectinload(CityDB.teams)],
        filters={
            "id_filter": UUID,
            "search": "name",
            "pagination_type": "limit_offset",
            "pagination_size": 20,
            "created_at": True,
            "updated_at": True,
            "sort_field": "name",
            "sort_order": "asc",
        },
    )

    @get(operation_id="GetCities")
    async def get_cities(
        self,
        cities_service: CityService,
        filters: Annotated[list[FilterTypes], Dependency(skip_validation=True)],
    ) -> OffsetPagination[City]:
        results, total = await cities_service.list_and_count(*filters)
        return cities_service.to_schema(results, total, filters, schema_type=City)

    @get(operation_id="GetCity", path="/{city_id:uuid}")
    async def get_city(
        self,
        cities_service: CityService,
        city_id: Annotated[UUID, Parameter(title="City ID", description="The city to retrieve.")],
    ) -> City:
        db_obj = await cities_service.get(city_id)
        return cities_service.to_schema(db_obj, schema_type=City)

    @post(operation_id="CreateCity", path="")
    async def create_city(
        self,
        cities_service: CityService,
        data: CityCreate
    ) -> City:
        db_obj = await cities_service.create(data.to_dict())
        return cities_service.to_schema(db_obj, schema_type=City)

    @put(operation_id="UpdateCity", path="/{city_id:uuid}")
    async def update_city(
        self,
        cities_service: CityService,
        data: CityUpdate,
        city_id: Annotated[
            UUID,
            Parameter(title="City ID", description="The city to update."),
        ],
    ) -> City:
        db_obj = await cities_service.update(item_id=city_id, data=data.to_dict())
        return cities_service.to_schema(db_obj, schema_type=City)

    @delete(operation_id="DeleteCity", path="/{city_id:uuid}")
    async def delete_city(
        self,
        cities_service: CityService,
        city_id: Annotated[
            UUID,
            Parameter(title="City ID", description="The city to delete."),
        ],
    ) -> None:
        await cities_service.delete(city_id)
