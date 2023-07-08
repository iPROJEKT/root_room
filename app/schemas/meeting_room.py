from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]

    @validator('name')
    def valid_name(cls, value: str):
        if value == '':
            raise ValueError('Не может быть пустым')
        if len(value) > 100:
            raise ValueError('Не может привышать 100 символов')
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomUpdate(MeetingRoomBase):
    pass


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
