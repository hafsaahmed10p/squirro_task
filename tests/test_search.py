import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app 

client = TestClient(app)

# Mock data
mock_document = {"text": "Sample document text"}
mock_doc_id = "1"
mock_retrieve_response = {"id": mock_doc_id, "content": "Sample document text"}
mock_search_response = [{"id": mock_doc_id, "score": 1.0, "text": "Sample document text"}]


@patch('app.es_service.es_service.search', return_value=mock_search_response)
def test_search_documents(mock_search):
    query = "Sample"
    k = 5
    response = client.get(f"/search/?query={query}&k={k}")
    assert response.status_code == 200
    assert response.json() == mock_search_response
    mock_search.assert_called_once_with(query, k, desc=True)

# Error handling tests
@patch('app.es_service.es_service.search', side_effect=Exception("Elasticsearch error"))
def test_search_documents_error(mock_search):
    query = "Sample"
    k = 5
    response = client.get(f"/search/?query={query}&k={k}")
    assert response.status_code == 500
    assert '{"error":"Internal Server Error","message":"An unexpected error occurred."}' == response.text