from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from dotenv import load_dotenv
import tiktoken
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model_client = OpenAIChatCompletionClient(model="gemini-1.5-flash-8b", api_key=api_key)


print("ok")