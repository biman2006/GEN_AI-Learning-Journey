from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=300)

documents = [
    "MS Dhoni is a legendary Indian wicketkeeper-batsman known for his calm leadership and finishing ability.",
    "Virat Kohli is one of India's greatest batsmen, famous for his consistency, aggressive style, and chasing ability.",
    "Rohit Sharma is an accomplished Indian batsman known for his elegant stroke play and remarkable ability to score big centuries.",
    "Jasprit Bumrah is one of India's best fast bowlers, recognized for his unique bowling action and deadly yorkers.",
    "Ravindra Jadeja is an outstanding Indian all-rounder known for his batting, left-arm spin bowling, and exceptional fielding."
]

query="Tell me about batsman"

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding], doc_embeddings)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is: ", score)