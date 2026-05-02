from litestar import Controller, get


class StadiumController(Controller):
    tags = ["Stadiums"]

    @get(path="api/v1/stadiums")
    async def get_stadiums(
        self,
    ):
        return {}
