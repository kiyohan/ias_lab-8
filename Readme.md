# Agentic Customer Support AI (Gemini Version)

## Overview

This project implements an Agentic AI system using:

* LangGraph (stateful graph execution)
* Gemini 2.5 Flash (LLM)
* Tool-based routing
* FastAPI backend
* Simple HTML frontend

The agent:

1. Understands customer messages
2. Classifies issue type
3. Routes to correct handler
4. Generates response
5. Escalates to human if needed

---

## Architecture

Components:

* LLM: Gemini 2.5 Flash
* Tools: Simulated business handlers
* Graph: LangGraph StateGraph
* Backend: FastAPI
* Frontend: Static HTML page

Flow:

User → Agent Node → Tool Node → Agent Node → Final Response

---

## Setup Instructions

### 1️⃣ Clone Project

```
git clone <repo_url>
cd agentic-support-ai/backend
```

---

### 2️⃣ Create Virtual Environment

Linux / Mac:

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add Gemini API Key

Create `.env` file inside backend folder:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Backend

```
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## Running the Frontend

Open:

```
frontend/index.html
```

in your browser.

---

## Example Inputs

* "My delivery is late"
* "I want a refund"
* "The app is not working"
* "This is unacceptable"

---

