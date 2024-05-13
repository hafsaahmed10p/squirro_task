
from pydantic import BaseModel


class SearchResponse(BaseModel):
    id: str
    score: float
    text: str
    