from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from common.city_types import LocationTypeEnum
from src.infrastructure.models.base import Base


class City(Base):

    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    type: Mapped[Enum] = mapped_column(Enum(LocationTypeEnum))

    name_eng: Mapped[str] = mapped_column(String(length=150), nullable=True)
    name_uk: Mapped[str] = mapped_column(String(length=150), nullable=True)
    name_ru: Mapped[str] = mapped_column(String(length=150), nullable=True)

    post_code: Mapped[str] = mapped_column(String(length=10), nullable=True)

    lng: Mapped[float] = mapped_column(nullable=True)
    lat: Mapped[float] = mapped_column(nullable=True)
    katottg: Mapped[str] = mapped_column(String(length=19))

    parent_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=True)
