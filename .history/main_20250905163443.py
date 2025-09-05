



# What is Tavily API?

# Tavily is a search API — ek AI-first search engine jo real-time information,
# web results, aur context-aware data fetch karta hai. Ye mainly agents,
# LLMs aur AI assistants ke liye banaya gaya hai taake 
# woh internet se fresh aur verified information la saken.






from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled,function_tool
from dotenv import load_dotenv
from tavily import TavilyClient
import requests
import asyncio
import os


load_dotenv(override=True)
set_tracing_disabled(disabled=True)
gemini_api = os.getenv("GEMINI_API_KEY")
weather_api = os.getenv("WEATHER_API_KEY")
if not gemini_api:
    raise ValueError("Gemini api is not found")



client = AsyncOpenAI(api_key=gemini_api,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

Model = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

@function_tool
def Tavily(query:str):
 print("Tavily Tool call")
 tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
 response = tavily_client.search(query=query,search_depth="advanced")

 print(response)




agent = Agent(name="Ratan lal",instructions="""
              You are a helpful Assistant
              """,model=Model,tools=[Tavily])

async def main():
    while True:
     msg = input("Enter your Sentences: ")

     result = await Runner.run(starting_agent=agent,input=msg)
     print(result.final_output)

     if msg == "exit":
        break

if __name__ == "__main__":
    asyncio.run(main())

