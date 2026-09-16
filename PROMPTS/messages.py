from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

import os

api_key=os.getenv("GROQ_API_KEY")

model=ChatGroq( model="openai/gpt-oss-120b",
    temperature=0,
    api_key=api_key)

messages=[
    SystemMessage(content="You are a help ful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)