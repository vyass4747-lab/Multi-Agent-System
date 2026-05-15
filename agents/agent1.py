from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from dotenv import load_dotenv
from tools.tool1 import web_search
load_dotenv()

llm = ChatMistralAI(model="mistral-small-2506")

def buid_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )



