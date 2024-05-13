import openai
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

openai.api_key=os.environ.get('OPEN_AI_API_KEY')
def generate_ans_from_docs(query: str, documents: List[str]):
    
    prompt = prompt = f"You are a chatbot who will answer this query {query} from the following results and contents. documents: {' '.join(documents)}. Only find the answer from the given documents like search from documents and infer from it. Do not talk about things that are not mentioned in the query"            
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo-16k",
        messages = [{"role" : "assistant", "content" : [{"type" : "text" , "text" : prompt}]}],
        max_tokens = 800,
        temperature = 0.2,
        top_p = 1.0,           
        n=1,                        
        stop="\n"  )
 
    if response.choices[0]:
        answer = response.choices[0].message.content.strip()
        return answer
    return f"Error! Could not get valid response from the AI Model"