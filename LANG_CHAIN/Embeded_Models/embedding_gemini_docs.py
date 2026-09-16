from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    output_dimensionality=1324
)

documents=[
    "Delhi is the Capital of India",
    "Kolkata is the Capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(
    documents
)

print(str(result))