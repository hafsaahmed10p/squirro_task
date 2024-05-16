import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

# Mock data
mock_document = {"text": "Sample document text"}
mock_doc_id = "1"
mock_retrieve_response = {"id": mock_doc_id, "content": "Sample document text"}

@patch('app.es_service.es_service.index_document', return_value=mock_doc_id)
def test_store_document(mock_index_document):
    response = client.post("/documents/", json=mock_document)
    assert response.status_code == 200
    assert response.json() == {"document_id": mock_doc_id}
    mock_index_document.assert_called_once_with(mock_document["text"])

@patch('app.es_service.es_service.retreive_document', return_value=mock_retrieve_response)
def test_retrieve_document_by_id(mock_retrieve_document):
    response = client.get(f"/documents/{mock_doc_id}")
    assert response.status_code == 200
    assert response.json() == mock_retrieve_response
    mock_retrieve_document.assert_called_once_with(mock_doc_id)


# Error handling tests
@patch('app.es_service.es_service.index_document', side_effect=Exception("Elasticsearch error"))
def test_store_document_error(mock_index_document):
    response = client.post("/documents/", json=mock_document)
    assert response.status_code == 200
    assert "Error occured while storing documents" in response.text

@patch('app.es_service.es_service.retreive_document', side_effect=Exception("Elasticsearch error"))
def test_retrieve_document_by_id_error(mock_retrieve_document):
    response = client.get(f"/documents/{mock_doc_id}")
    assert response.status_code == 200
    assert "Error Occured while retrieving documents" in response.text