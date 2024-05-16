import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app 

client = TestClient(app)

# Mock data
mock_query = "Sample query"
mock_documents = [{"text": "Sample document1"}, {"text": "Sample document2"}]
mock_generated_answer = "Generated answer"

@patch('app.es_service.es_service.search', return_value=mock_documents)
@patch('app.openai_service.openai_service.generate_ans_from_docs', return_value=mock_generated_answer)
def test_generate_answer_from_docs(mock_generate_ans, mock_search):
    response = client.get(f"/generate-answer/?query={mock_query}&k=5")
    assert response.status_code == 200
    assert response.json() == {"answer": mock_generated_answer}
    mock_search.assert_called_once_with(mock_query, 5)



@patch('app.openai_service.openai_service.generate_ans_from_docs', side_effect=Exception("OpenAI error"))
def test_generate_answer_from_docs_error_openai(mock_generate_ans):
    response = client.get(f"/generate-answer/?query={mock_query}&k=5")
    assert response.status_code == 500
    assert '{"error":"Internal Server Error","message":"An unexpected error occurred."}' == response.text