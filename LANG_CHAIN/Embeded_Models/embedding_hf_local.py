from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents=["Delhi is the capital of INDIA",
           "CSK is the greatest team in the ipl",
           "THALA IS THE CAPTAIN OF CSK"]

print(str(embeddings.embed_documents(documents)))

