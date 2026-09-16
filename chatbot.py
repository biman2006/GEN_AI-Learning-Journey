import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print(
        "Missing GROQ_API_KEY. Create a .env file in the project root with:\n"
        "GROQ_API_KEY=your_key_here"
    )
    raise SystemExit(1)

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=api_key,
)

chat_hist=[SystemMessage(content="You Are A HelpFul AI Assistant")]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer briefly, clearly, and simply."),
    ("user", "{question}"),
])

while True:
    user = input("You: ").strip()
    chat_hist.append(HumanMessage(content=user))
    if not user or user.lower() == "exit":
        break

    response = model.invoke(prompt.format_messages(question=chat_hist))
    chat_hist.append(response.content)
    print("AI:", response.content)
print(chat_hist)