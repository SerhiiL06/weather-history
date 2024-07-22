from loguru import logger
from sqlalchemy import and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from common.city_types import LocationTypeEnum
from src.infrastructure.models.city import City
from src.repository.exceptions.exc import DoesntExists


class CityRepository:

    async def get_coordinate_by_name(self, name: str, session: AsyncSession) -> City:

        query = select(City.id, City.lat, City.lng).where(
            and_(
                or_(
                    City.name_eng.ilike(name),
                    City.name_ru.ilike(name),
                    City.name_uk.ilike(name),
                ),
                City.type.in_(
                    (
                        LocationTypeEnum.CAPITAL_CITY,
                        LocationTypeEnum.CITY,
                        LocationTypeEnum.DISTRICT,
                        LocationTypeEnum.VILLAGE,
                    )
                ),
            )
        )

        result = await session.execute(query)

        city = result.mappings().first()

        if city is None:
            raise DoesntExists(City, 1)

        return city
