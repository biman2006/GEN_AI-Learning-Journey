from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 

load_dotenv()

model=ChatOpenAI(model='gpt-4o-mini', temperature=0, max_completion_tokens=10) #Temperature is parameter that controls randomness of a language model's output it effects how creative or deterministic the response are 

result=model.invoke("What is the capital of India")

print(result) 

