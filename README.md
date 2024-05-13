----Setup the application-----

# Create your virtual environment using the following

python -m venv venv

Activate your virtual env

venv\Scripts\activate 

# Install the necessary packages

pip install -r requirements.txt



---- Create .env file -----

Create .env file With following variables

# OpenAI API Key 
# You can get your API key from here -> https://platform.openai.com/api-keys 
OPEN_AI_API_KEY="your_openai_api_key"

# URL For Elastic Search
# For Cloud API Key and endpoint, Checkout this guide -> 

ELASTIC_SEARCH_ENDPOINT="your_elastic_search_endpoint"
ELASTIC_SEARCH_API_KEY="your_elastic_search_api_key"



----- Using Elastic Search Locally --------

You can also run elastic search locally
Follow this guide to set it up on your machine ->  https://www.elastic.co/guide/en/elasticsearch/reference/7.17/install-elasticsearch.html

# Default URL: "http://localhost:9200"

If running it locally, use this line of code on main.py instead, for making elastic search connection

es = Elasticsearch("http://localhost:9200")






