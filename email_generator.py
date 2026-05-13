from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["content", "customer_name", "agent_name"],
    template="""
You are an AI assistant optimized to write concise, professional, and friendly emails.

Write a professional email to {customer_name}.

Content:
{content}

Signature:
{agent_name}
"""
)

content = input("Email content: ")
customer = input("Customer name: ")
agent = input("Agent name: ")

final_prompt = prompt.format(
    content=content,
    customer_name=customer,
    agent_name=agent
)

response = llm.invoke(final_prompt)
print(response.content)