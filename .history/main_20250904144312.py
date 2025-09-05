# from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled,function_tool
# from dotenv import load_dotenv
# import requests
# import asyncio
# import os


# load_dotenv(override=True)
# set_tracing_disabled(disabled=True)
# gemini_api = os.getenv("GEMINI_API_KEY")
# weather_api = os.getenv("WEATHER_API_KEY")
# if not gemini_api:
#     raise ValueError("Gemini api is not found")

# names = ["Karachi","Lahore","Islamabad","Pindi","Sindh","Peshawar","Kashmir"]

# @function_tool
# def get_weather(city:str = names) -> str :
#     print("Weather Tool Fire...")

#     url = " http://api.weatherapi.com/v1/current.json"

#     params = {
       
#        "q":city,
#         "key":weather_api


#   }
     
#     try:
     
#      Response = requests.get(url,params=params)
#      Response.raise_for_status()
#      data = Response.json()


#      temp = data["current"]["temp_c"]
#      des = data["current"]["condition"]["text"]

#      return f"The Current {city} temperature {temp} is {des}"
    
#     except Exception :
#        return f"The current temperature not found"
    

# @function_tool
# def plus(a,b):
#    print("Plus Tool Fire...")
#    return f"The answer is {a + b}"
   
    

# client = AsyncOpenAI(api_key=gemini_api,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# Model = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

# agent = Agent(name="Ratan lal",instructions="You are a helpful Assistant",model=Model,tools=[get_weather,plus])

# async def main():
#     result = await Runner.run(starting_agent=agent,input=input("Enter your Sentences::"))
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())





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
async def Tavily():




 tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
 response = tavily_client.search("Who is Leo Messi?")

print(response)




agent = Agent(name="Ratan lal",instructions="You are a helpful Assistant",model=Model)

async def main():
    result = await Runner.run(starting_agent=agent,input=input("Enter your Sentences::"))
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

