import pandas as pd

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Integer

from app.models.db import Base
from app.models.db import database
from app.models.rate import Rate
from app.utils.recommendation import Recommendation


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(String)
    title = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, id, user_id, title, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def find_all_recommended(user_id: str=None, limit: int=None):
        session = database.connect_db()
        query = session.query(Video, Rate).filter(Video.id == Rate.video_id).limit(1000).statement
        df = pd.read_sql(query, session.bind)
        df.columns = ['id', 'user_id', 'title', 'created_at', 'updated_at', 'rate_id', 'rate_user_id', 
            'rate_video_id', 'rate_rate', 'rate_created_at', 'rate_updated_at']

        recommender = Recommendation()
        rows = recommender.predict(df=df, dataset_columns=['rate_user_id', 'rate_video_id', 'rate_rate'], 
            item_id='rate_video_id', user_id=user_id, limit=limit, result_model=Video)
        session.close()

        if rows is None: return []

        return rows

    @classmethod
    def init_from_df(cls, df):
        return cls(
            id=df['id'],
            user_id=df['user_id'],
            title=df['title'],
            created_at=df['created_at'],
            updated_at=df['updated_at'],
        )

    @property
    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
