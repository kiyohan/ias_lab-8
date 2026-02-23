from langgraph.graph import StateGraph, END
from agent import AgentState, create_llm, create_agent_node

def build_graph():

    llm = create_llm()
    agent_node = create_agent_node(llm)

    workflow = StateGraph(AgentState)

    workflow.add_node("agent", agent_node)

    workflow.set_entry_point("agent")
    workflow.add_edge("agent", END)

    return workflow.compile()