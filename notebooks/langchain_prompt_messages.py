import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    api_version="v1beta"
)

messages = [
    SystemMessage("You are a python expert"),
    HumanMessage("Explain list in 2 lines"),
    AIMessage("Cherry blossoms bloom...")
]

response = llm.invoke(messages)

print(response.content)