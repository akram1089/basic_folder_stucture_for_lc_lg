from .model import get_llm

llm = get_llm()

def simple_chain(text: str) -> str:
    result = llm.invoke(text)
    return result.content
