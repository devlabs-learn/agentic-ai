from langgraph.graph import StateGraph, START, END

class AnalysisState(dict):
    task: str
    research_output: str
    summary_output: str
    blog_output: str

def researcher_agent(state: AnalysisState) -> AnalysisState:
    state['research_output'] = f"Researching {state['task']}..."
    return state

def summarizer_agent(state: AnalysisState) -> AnalysisState:
    state['summary_output'] = f"Summarizing research on {state['research_output']}..."
    return state

def blogger_agent(state: AnalysisState) -> AnalysisState:
    state['blog_output'] = f"Writing blog post based on {state['summary_output']}..."
    return state

graph = StateGraph(AnalysisState)

# Add available agents as nodes in the graph
graph.add_node("researcher", researcher_agent)
graph.add_node("summarizer", summarizer_agent)
graph.add_node("blogger", blogger_agent)

# Define the flow of the graph by adding edges between nodes
# Flow is: START -> researcher -> summarizer -> blogger -> END
# Flow diagram:
graph.add_edge(START, "researcher")
graph.add_edge("researcher", "summarizer")
graph.add_edge("summarizer", "blogger")
graph.add_edge("blogger", END)

# Execute the graph with an initial state
graph = graph.compile()
result = graph.invoke(AnalysisState(task="the impact of AI on society"))

print("Final State:", result)
print("Blog Output:", result['blog_output'])


