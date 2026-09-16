from langchain_openai import OpenAI ## Integration package bw langchain and OPENAI 
from dotenv import load_dotenv 

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke("what is the capital of INDIA")  ## invoke() simply means “send this input to the LLM and get its response.”
print(result)