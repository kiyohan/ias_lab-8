# agent.py
from typing import TypedDict, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]


def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0,
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )


def create_agent_node(llm):

    async def call_agent(state: AgentState):

        messages = state["messages"]
        user_message = messages[-1].content

        # Step 1: Ask LLM to classify issue
        classification_prompt = f"""
        Classify the following customer message into one of:
        delivery, refund, technical, other

        Message: "{user_message}"

        Only respond with one word.
        """

        classification = await llm.ainvoke(
            [HumanMessage(content=classification_prompt)]
        )

        issue_type = classification.content.strip().lower()

        # Step 2: Route in Python (not Gemini function calls)

        if issue_type == "delivery":
            response_text = "Your order is in transit and will arrive within 2 days."
        elif issue_type == "refund":
            response_text = "Your refund request is approved. Amount will be credited in 5-7 business days."
        elif issue_type == "technical":
            response_text = "Please try clearing cache and reinstalling the app. Contact support if issue persists."
        else:
            response_text = "Your issue has been escalated to a human support executive."

        return {
            "messages": messages + [HumanMessage(content=response_text)]
        }

    return call_agent