from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HUGGING_FACE_API_KEY")
if not hf_token:
    raise ValueError("HUGGING_FACE_API_KEY is missing from .env")

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of India?")

print(result.content)