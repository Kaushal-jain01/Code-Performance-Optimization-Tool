import os

from langchain_core.messages import HumanMessage

from constants import openai_key, langchain_api_key
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = openai_key
os.environ['LANGCHAIN_API_KEY'] = langchain_api_key
os.environ['LANGCHAIN_TRACING_V2']="true"

model = ChatOpenAI(temperature=0)

def llm(x):
    return model.invoke(x).content

