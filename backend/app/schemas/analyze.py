from pydantic import BaseModel
from typing import Optional


class AnalyzeRequest(BaseModel):
    passage_id: str
    passage_text: str
    passage_title: str

# Phân tích kết quả phát âm
class WordResult(BaseModel):
    word: str
    spoken: Optional[str] = None
    correct: bool
    similarity: float
    severity: str  # correct | minor | major | missing

# Phân tích lỗi phát âm theo mẫu
class PatternError(BaseModel):
    pattern: str
    description: str
    examples: list[str]
    count: int

# Phản hồi tổng thể kết quả
class AnalyzeResponse(BaseModel):
    transcript: str
    score: float
    word_results: list[WordResult]
    patterns: list[PatternError]
    total_words: int
    correct_words: int
    session_id: Optional[int] = None