from fastapi import HTTPException
from config import config
from elasticsearch import Elasticsearch
from typing import List



es = Elasticsearch(
  config.ELASTIC_SEARCH_ENDPOINT,
  api_key = config.ELASTIC_SEARCH_API_KEY
)

es_index_name = config.ES_INDEX_NAME

def index_document(document_text: str) -> str:
    doc = {"text": document_text}
    res = es.index(index=es_index_name, body=doc)
    doc_id = res['_id']
    return doc_id

def retreive_document(id: str):
    res = es.get(index=es_index_name, id=id)
    if res['found']:
        return {"id": id, "content": res['_source']['text']}
    else:
        raise HTTPException(status_code=404, detail="Document Not Found")

def search(query: str, k: int = 5, desc:bool = True) -> List[dict]:
    if (k<0):
        raise HTTPException(status_code=400, detail="K must be greater than equals to 0")  
    try: 
        sort_order = "desc" if desc else "asc"
        res = es.search(index=es_index_name, body={"query": {"match": {"text": query}}, "size": k, "sort": [{"_score": {"order": sort_order}}] })
        hits = res['hits']['hits']
        results = [{"id": hit['_id'], "score": hit['_score'], "text" : hit['_source']['text']} for hit in hits]
        return results
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")