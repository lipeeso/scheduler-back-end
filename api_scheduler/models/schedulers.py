from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Numeric, Integer, Text, func
from enum import Enum
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from api_scheduler.core.database import Base
if TYPE_CHECKING:
    from api_scheduler.models.users import User

class SchedulerType(str, Enum):
    CONFIRMED = "confirmed"
    PENDENT = "pending"
    CANCELED = "canceled"

class ServiceType(str, Enum):
    DEFAULT = "default"
    URGENT = "urgent"

class Scheduler(Base):
    __tablename__ = "schedulers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    service: Mapped[ServiceType] = mapped_column(String(20))
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    value: Mapped[int] = mapped_column(Numeric(10,2))
    status: Mapped[SchedulerType] = mapped_column(String(20))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    update_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    owner: Mapped["User"] = relationship("User", back_populates="schedulers")

