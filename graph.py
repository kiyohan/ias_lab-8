from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from agent import AgentState, create_llm, create_agent_node
from tools import (
    classify_issue,
    delivery_handler,
    refund_handler,
    technical_handler,
    escalate_to_human,
)

def build_graph():

    tools = [
        classify_issue,
        delivery_handler,
        refund_handler,
        technical_handler,
        escalate_to_human,
    ]

    llm = create_llm()
    agent_node = create_agent_node(llm, tools)
    tool_node = ToolNode(tools)

    def should_continue(state: AgentState):
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END

    workflow = StateGraph(AgentState)

    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {"tools": "tools", END: END}
    )

    workflow.add_edge("tools", "agent")

    return workflow.compile()