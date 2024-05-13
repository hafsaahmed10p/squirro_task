from fastapi import FastAPI, HTTPException, Query
from typing import List
from models import Document, SearchResponse, RetrieveDocumentResponse, StoreDocumentResponse, AnswerQueryResponse
from elasticsearch import Elasticsearch
from open_ai_answer_retrieval  import generate_ans_from_docs
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Squirro Document Search Task")
 
es = Elasticsearch(
  os.environ.get("ELASTIC_SEARCH_ENDPOINT"),
  api_key = os.environ.get("ELASTIC_SEARCH_API_KEY")
)

es_index_name = "documents-index"

# Store documents (texts) 
@app.post("/documents/", response_model=StoreDocumentResponse)
def store_document(document: Document):
    doc_id = index_document(document.text)
    return StoreDocumentResponse(doc_id= doc_id)
 
# Retrieve document by id
@app.get("documents/{id}", response_model=RetrieveDocumentResponse)
def retrieve_document_by_id(id: str):
    res = es.get(es_index_name, id )
    if res['found']:
        return RetrieveDocumentResponse( id=id, content=res['_source']['text'])
    else:
        raise HTTPException(404, "Document Not Found")

# Search top k documents 
@app.get("/search/", response_model=List[SearchResponse])
def search_documents(query: str, k: int = Query(5, description="Top K documents to choose the results from")):
    results = search(query, k)   
    search_responses = [SearchResponse(id=result["document_id"], score=result["score"], text=result["text"]) for result in results]
    return search_responses

# Generate Answer from the top K documents using OpenAI LLM Model
@app.get("/generate-answer/", response_model=AnswerQueryResponse)
def generate_answer_from_docs(query: str, k : int = Query(5, description="Top K documents to choose the results from")):
    results = search(query, k)
    documents = [result["text"] for result in results]
    result = generate_ans_from_docs(query, documents)
    return AnswerQueryResponse(answer=result)

def index_document(document_text: str) -> str:
    doc = {"text": document_text}
    res = es.index(index=es_index_name, body=doc)
    doc_id = res['_id']
    return doc_id
 

def search(query: str, k: int = 5) -> List[dict]:
    if (k<0):
        raise HTTPException(status_code=400, detail="K must be greater than equals to 0")  
    res = es.search(index=es_index_name, body={"query": {"match": {"text": query}}, "size": k})
    hits = res['hits']['hits']
    results = [{"document_id": hit['_id'], "score": hit['_score'], "text" : hit['_source']['text']} for hit in hits]
    return results
 

