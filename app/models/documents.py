
from pydantic import BaseModel


# Request Models
class Document(BaseModel):   
    text: str


# Response Models
class RetrieveDocumentResponse(BaseModel):
    id: str
    content: str  
    
class StoreDocumentResponse(BaseModel):
    document_id: str