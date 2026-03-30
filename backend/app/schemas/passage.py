from pydantic import BaseModel


class PassageOut(BaseModel):
    id: str
    title: str
    text: str
    difficulty: str
    tags: list[str]
    word_count: int

    class Config:
        from_attributes = True