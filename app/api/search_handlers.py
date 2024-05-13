# app/search_handlers.py
from fastapi import APIRouter
from typing import List
from app.es_service import es_service
from app.models.search import SearchResponse

router = APIRouter()


@router.get("/search/", response_model=List[SearchResponse])
def search_documents(query: str, k: int = 5, desc: bool = True):
    try:
        results = es_service.search(query, k, desc=desc)
        search_responses = [
            SearchResponse(id=result["document_id"], score=result["score"], text=result["text"])
            for result in results
        ]
        return search_responses
    except Exception as e:
        return(f"Error Occured while searching documents: {str(e)} " )
