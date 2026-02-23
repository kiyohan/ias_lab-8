# main.py
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from graph import build_graph

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

agent = build_graph()

# In-memory session storage
sessions = {}

class Query(BaseModel):
    message: str
    session_id: str | None = None


@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")


@app.post("/chat")
async def chat(query: Query):

    session_id = query.session_id or str(uuid.uuid4())

    if session_id not in sessions:
        sessions[session_id] = []

    # Append user message to current state
    sessions[session_id].append(HumanMessage(content=query.message))

    try:
        result = await agent.ainvoke({
            "messages": sessions[session_id]
        })
    except Exception as e:
        print("Agent failed:", e)
        return {
            "response": "The agent encountered an internal error.",
            "session_id": session_id
        }

    if not result or "messages" not in result:
        return {
            "response": "Agent returned empty response.",
            "session_id": session_id
        }

    from langchain_core.messages import AIMessage

    sessions[session_id] = result["messages"]

    last_message = sessions[session_id][-1]
    content = last_message.content

    return {
        "response": content,
        "session_id": session_id
    }