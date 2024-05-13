from fastapi import Query
from pydantic import BaseModel, Field


# Request Models
class Document(BaseModel):   
    text: str


# Response Models
class RetrieveDocumentResponse(BaseModel):
    id: int
    content: str  
    
class StoreDocumentResponse(BaseModel):
    doc_id: int

class SearchResponse(BaseModel):
    id: str
    score: float
    text: str
    
class AnswerQueryResponse(BaseModel):
    answer:str