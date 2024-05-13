# app/answer_handlers.py
from fastapi import APIRouter
from app.models.answer import AnswerQueryResponse
from app.es_service import es_service
from app.openai_service import openai_service

router = APIRouter()


@router.get("/generate-answer/", response_model=AnswerQueryResponse)
def generate_answer_from_docs(query: str, k: int = 5):
    try:       
        results = es_service.search(query, k)
        documents = [result["text"] for result in results]
        result = openai_service.generate_ans_from_docs(query, documents)
        return AnswerQueryResponse(answer = result)
    except Exception as e:
        return(f"Error Occured while generating answers: {str(e)} " )
