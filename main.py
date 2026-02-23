import os
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

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

    if not query.session_id:
        session_id = str(uuid.uuid4())
    else:
        session_id = query.session_id

    if session_id not in sessions:
        sessions[session_id] = []

    # Add user message
    sessions[session_id].append(HumanMessage(content=query.message))

    # Call agent
    result = await agent.ainvoke({
        "messages": sessions[session_id]
    })

    if not result or "messages" not in result:
        return {
            "response": "Something went wrong.",
            "session_id": session_id
        }

    # 🔥 IMPORTANT: overwrite with returned state
    sessions[session_id] = result["messages"]

    # Final message
    final_message = sessions[session_id][-1]

    return {
        "response": final_message.content if final_message.content else "No response generated.",
        "session_id": session_id
    }