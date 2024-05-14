# ----Setup the application-----

### Create your virtual environment using the following commands

```python -m venv venv```

Activate your virtual env

```venv\Scripts\activate``` 

### Install the necessary packages

```pip install -r requirements.txt```



# ---- Create .env file -----

Create .env file With following variables

#### OpenAI API Key 
*You can get your API key from here -> https://platform.openai.com/api-keys*

```OPEN_AI_API_KEY="your_openai_api_key"```

### URL For Elastic Search
* For Cloud API Key and endpoint, you need to have elastic cloud. Follow this link for further details -> https://www.elastic.co/cloud

```ELASTIC_SEARCH_ENDPOINT="your_elastic_search_endpoint"```

```ELASTIC_SEARCH_API_KEY="your_elastic_search_api_key"```



# ----- Using Elastic Search Locally --------

You can also run elastic search locally
*Follow this guide to set it up on your machine ->  https://www.elastic.co/guide/en/elasticsearch/reference/7.17/install-elasticsearch.html*

 Default URL: "http://localhost:9200"

*If running it locally, use this line of code on main.py instead, for making elastic search connection*

```es = Elasticsearch("http://localhost:9200")```

# ----- Running the App --------

*Use the following command to run the code*

```uvicorn main:app --reload``` 

# ---- Testing -----------

*You can test the APIs here*

http://127.0.0.1:8000/docs

**1. For Storing Document**

  **URL**: *POST/documents/*
  
  __Body__
  
  document (required): JSON object containing the text of the document.
  
  *Example*
{
  "text": "There is a novel called Mission 007 written by Alex James"
}
  Example URL: http://your-api-url/documents/

**2. Retrieve Document by ID Endpoint**

  **URL:** *GET/documents/{id}*
  
  Path Parameter:
  
   id (required): The ID of the document to retrieve.
   
   Example URL: http://your-api-url/documents/document_id_here

**3. Search Documents Endpoint**'

  **URL:** *GET/search/*
  
  Parameters:
  
   query (required): The query string (sentence or keyword) to search for documents.
   
   k (optional): The number of documents to retrieve (default is 5).
     
   desc (optional): Whether to sort the retrieved documents in descending order (default is True).
   
   Example URL: http://your-api-url/search/?query=your_query_here&k=5



**4. Generate Answer Endpoint**

  __URL:__ *GET/generate-answer/*
  
  Parameters:
  
  query (required): The query for which you want to generate an answer.
  
  k (optional): Number of documents to retrieve from Elasticsearch (default is 5).

  Example Query -> "what do you know about mission 007"
  
  Example URL: http://your-api-url/generate-answer/?query=your_query_here&k=5&desc=True






