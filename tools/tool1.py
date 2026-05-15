from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
from rich import print
import requests
import os
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)->str:
    """search the web for reliable and recent news on a topic . return topic , snippet and url."""
    results = tavily.search(query=query , max_results=5)

    output = []

    for r in results['results']:
        output.append(
            f"title:{r['title']}\n url:{r['url']}\n snippet:{r['content']}"
        
        )

    return "\n------\n".join(output)

