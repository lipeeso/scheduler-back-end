from typing import List, Optional
from pydantic import BaseModel




class SchedulerSchema(BaseModel):
    name: str
    service: str
    description: Optional[str] = None
    value: int
    status: str

class SchedulerUpdateSchema(BaseModel):
    name: Optional[str] = None
    service: Optional[str] = None
    description: Optional[str] = None
    value: Optional[int] = None
    status: Optional[str] = None

class SchedulerPublicSchema(BaseModel):
    name: str
    service: str
    description: Optional[str] = None
    value: int
    status: str

class SchedulerListPublicSchema(BaseModel):
    schedulers: List[SchedulerPublicSchema]
    offset: int
    limit: int