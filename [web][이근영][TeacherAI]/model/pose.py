from app import db
from datetime import datetime
from .base import Base

class Pose(Base):
    __tablename__ = 'pose'

    id = db.Column(db.BigInteger, primary_key=True)
    video_id = db.Column(db.BigInteger)
    start_time = db.Column(db.BigInteger)
    end_time = db.Column(db.BigInteger)
    content = db.Column(db.Text)