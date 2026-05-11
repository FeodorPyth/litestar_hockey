from __future__ import annotations
from typing import TYPE_CHECKING, Annotated
from uuid import UUID

from litestar import Controller, get, post, put, delete
from litestar.params import Dependency, Parameter
from sqlalchemy.orm import selectinload

from db.models import StadiumDB
from domain.models import Stadium, StadiumCreate, StadiumUpdate
from domain.services import StadiumService
from lib.deps import create_service_dependencies

if TYPE_CHECKING:
    from advanced_alchemy.filters import FilterTypes
    from advanced_alchemy.service.pagination import OffsetPagination


class StadiumController(Controller):
    tags = ["Stadiums"]
    path = "/stadiums"
    dependencies = create_service_dependencies(
        StadiumService,
        key="stadiums_service",
        load=[selectinload(StadiumDB.teams), selectinload(StadiumDB.city)],
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

    @get(operation_id="GetStadiums")
    async def get_stadiums(
        self,
        stadiums_service: StadiumService,
        filters: Annotated[list[FilterTypes], Dependency(skip_validation=True)],
    ) -> OffsetPagination[Stadium]:
        results, total = await stadiums_service.list_and_count(*filters)
        return stadiums_service.to_schema(results, total, filters, schema_type=Stadium)

    @get(operation_id="GetStadium", path="/{stadium_id:uuid}")
    async def get_stadium(
        self,
        stadiums_service: StadiumService,
        stadium_id: Annotated[UUID, Parameter(title="Stadium ID", description="The stadium to retrieve.")],
    ) -> Stadium:
        db_obj = await stadiums_service.get(stadium_id)
        return stadiums_service.to_schema(db_obj, schema_type=Stadium)

    @post(operation_id="CreateStadium", path="")
    async def create_stadium(
        self,
        stadiums_service: StadiumService,
        data: StadiumCreate
    ) -> Stadium:
        db_obj = await stadiums_service.create(data.to_dict())
        db_obj = await stadiums_service.get(
            db_obj.id,
            load=[selectinload(StadiumDB.teams), selectinload(StadiumDB.city)]
        )
        return stadiums_service.to_schema(db_obj, schema_type=Stadium)

    @put(operation_id="UpdateStadium", path="/{stadium_id:uuid}")
    async def update_stadium(
        self,
        stadiums_service: StadiumService,
        data: StadiumUpdate,
        stadium_id: Annotated[
            UUID,
            Parameter(title="Stadium ID", description="The stadium to update."),
        ],
    ) -> Stadium:
        db_obj = await stadiums_service.update(item_id=stadium_id, data=data.to_dict())
        db_obj = await stadiums_service.get(
            db_obj.id,
            load=[selectinload(StadiumDB.teams), selectinload(StadiumDB.city)]
        )
        return stadiums_service.to_schema(db_obj, schema_type=Stadium)

    @delete(operation_id="DeleteStadium", path="/{stadium_id:uuid}")
    async def delete_stadium(
        self,
        stadiums_service: StadiumService,
        stadium_id: Annotated[
            UUID,
            Parameter(title="Stadium ID", description="The stadium to delete."),
        ],
    ) -> None:
        await stadiums_service.delete(stadium_id)
