from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()
from tools.tool2  import scrape_webpage

llm = ChatMistralAI(model="mistral-small-2506")

def buid_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_webpage]
    )

