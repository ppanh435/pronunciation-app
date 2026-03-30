from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Text
from sqlalchemy.sql import func
from app.db.database import Base

class Passage(Base):
    __tablename__ = "passages"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    difficulty = Column(String, nullable=False)
    tags = Column(JSON, nullable=False)
    word_count = Column(Integer, nullable=False, default=0)
    
class PracticeHistory(Base):
    __tablename__ = "practice_history"

    id = Column(Integer, primary_key=True, index=True)
    passage_id = Column(String, nullable=False)
    passage_title = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    transcript = Column(Text, nullable=False)
    word_results = Column(JSON, nullable=False)
    patterns = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())