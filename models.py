from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base
from datetime import datetime

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String)
    summary = Column(Text)
    sentiment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)