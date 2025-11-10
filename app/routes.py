from fastapi import APIRouter
from .llm.chain import simple_chain
from .llm.graph import run_graph

router = APIRouter()

@router.post('/chat')
async def chat(input_text: str):
    return {'response': simple_chain(input_text)}

@router.post('/graph')
async def graph_run(input_text: str):
    return {'response': run_graph(input_text)}
