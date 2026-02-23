# Agentic Customer Support AI  
Lab Assignment 8 — Agentic AI (LangGraph)

## 1. Problem Statement

Build an Agentic AI for first-level customer support in an e-commerce store.

The agent must:

1. Understand a customer message
2. Classify the issue type (delivery, refund, technical, other)
3. Route to the correct handler
4. Generate an appropriate response
5. Escalate to a human when required

---

## 2. Selected Use Case

**Customer Support – E-commerce**

Input: Free-text customer messages such as:

- “Where is my order?”
- “I want a refund.”
- “The app crashes on login.”

Goal: Automate first-level issue handling and routing using an Agentic AI architecture.

---

## 3. High-Level Architecture

Agent = LLM + Routing Logic + State + Graph Control

### Components

### 🔹 LLM (Gemini 1.5 Flash)
Used only for reasoning and issue classification.

### 🔹 Routing Logic (Python)
Based on the LLM’s classification result, the system routes to:

- Delivery handler
- Refund handler
- Technical handler
- Escalation

### 🔹 State (Session Memory)
- Stored per session using UUID
- Maintained as conversation history
- Graph output is treated as the single source of truth

### 🔹 Graph (LangGraph)
- Single Agent node
- Controlled execution
- Clean state transitions

---

## 4. System Flow

1. User sends message from frontend.
2. Backend appends HumanMessage to session state.
3. Agent is invoked using LangGraph.
4. LLM classifies the issue.
5. Python routing logic selects appropriate handler.
6. Response is returned.
7. Session state is updated.

---

## 5. Technology Stack

- LangGraph
- LangChain
- Gemini 1.5 Flash (Google Generative AI)
- FastAPI
- Uvicorn
- Python-dotenv
- HTML + JavaScript frontend

---

## 6. Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your_repo_url>
cd <project_folder>
````

---

### 2️⃣ Create Virtual Environment (Python 3.11 Required)

```bash
conda create -n agent311 python=3.11
conda activate agent311
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Gemini API Key

Create `.env` file in project root:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 7. Run the Application

```bash
uvicorn main:app
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 8. Example Test Cases

| Input                | Expected Behavior         |
| -------------------- | ------------------------- |
| Where is my order?   | Delivery handler response |
| I want a refund      | Refund handler response   |
| App not working      | Technical troubleshooting |
| This is unacceptable | Escalation                |

---

## 9. Design Decisions

* Avoided Gemini function-calling to ensure protocol stability.
* LLM used only for classification (controlled reasoning).
* Routing handled in Python for reliability.
* Session memory stored in-memory (lab requirement).
* Graph output treated as authoritative state.

---

## 10. Known Limitations

* Session memory is in-memory (not persistent).
* API quotas apply to Gemini usage.
* No database integration (simulated handlers only).

---
