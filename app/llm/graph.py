from langgraph.graph import StateGraph, END

def process(state):
    return {'output': f"Graph-processed: {state.get('input')}"}

def run_graph(input_text):
    graph = StateGraph()
    graph.add_node('process', process)
    graph.add_edge('process', END)
    graph.set_entry_point('process')
    machine = graph.compile()
    result = machine.invoke({'input': input_text})
    return result['output']
