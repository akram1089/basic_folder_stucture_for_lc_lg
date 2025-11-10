from langchain_openai import ChatOpenAI
from ..config import settings

def get_llm():
    return ChatOpenAI(model='gpt-3.5-turbo', temperature=0.3, openai_api_key=settings.OPENAI_API_KEY)
