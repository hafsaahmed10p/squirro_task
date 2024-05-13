import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY=os.environ.get("OPEN_AI_API_KEY")
ELASTIC_SEARCH_ENDPOINT=os.environ.get("ELASTIC_SEARCH_ENDPOINT")
ELASTIC_SEARCH_API_KEY=os.environ.get("ELASTIC_SEARCH_API_KEY")
ES_INDEX_NAME=os.environ.get("ES_INDEX_NAME")