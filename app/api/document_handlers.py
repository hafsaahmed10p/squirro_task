from fastapi import APIRouter, HTTPException
from app.models.documents import Document, RetrieveDocumentResponse
from app.es_service import es_service

router = APIRouter()

@router.post("/documents/")
def store_document(document: Document):
    try:
        doc_id = es_service.index_document(document.text)
        return {"document_id": doc_id}
    except Exception as e:
        return(f"Error occured while storing documents: {str(e)}")

@router.get("/documents/{id}")
def retrieve_document_by_id(id: str):
    try:
        result =  es_service.retreive_document(id) 
        return RetrieveDocumentResponse(id=result['id'], content=result['content'])
    except Exception as e:
        return(f"Error Occured while retrieving documents: {str(e)} " )
  
   