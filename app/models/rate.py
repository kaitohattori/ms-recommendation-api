from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Integer

from app.models.db import Base


class Rate(Base):
    __tablename__ = "rates"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(String)
    video_id = Column(Integer)
    value = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, id, user_id, video_id, value, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.video_id = video_id
        self.value = value
        self.created_at = created_at
        self.updated_at = updated_at
