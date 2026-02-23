from typing import TypedDict, Sequence
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]

def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

def create_agent_node(llm, tools):

    llm_with_tools = llm.bind_tools(tools)

    async def call_agent(state: AgentState):
        response = await llm_with_tools.ainvoke(state["messages"])
        return {"messages": [response]}  # 🔥 only return new message

    return call_agent