from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=2
)

result=model.invoke("Who is the captain of india who won all icc trophies except test?")
print(result.content)