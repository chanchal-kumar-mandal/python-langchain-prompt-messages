import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate  # Correct import

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    api_version="v1beta"
)

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {role} expert."),
    ("human", "Explain {topic} in 2 lines.")
])

# Format prompt with variables and invoke LLM
chain = prompt | llm
response = chain.invoke({"role": "Python", "topic": "list comprehension"})

print(response.content)