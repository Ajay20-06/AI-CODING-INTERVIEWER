# 🚀 AI Coding Interview Agent

An Agentic AI-powered coding interview platform that simulates real technical interviews, evaluates candidate responses, provides hints, generates follow-up questions, and supports voice-based interactions.

---

## 🌟 Overview

AI Coding Interview Agent is designed to replicate a real software engineering interview experience.

The system leverages multiple AI agents working together to:

- Ask Data Structures & Algorithms questions
- Evaluate candidate solutions
- Analyze problem-solving approaches
- Provide progressive hints
- Generate follow-up interview questions
- Conduct voice-based interviews
- Deliver detailed interview feedback

---

## 🏗️ Architecture

```text
Candidate
    │
    ▼
Interviewer Agent
    │
    ▼
Evaluator Agent
    │
    ├── Score Generation
    ├── Complexity Analysis
    └── Feedback
    │
    ▼
Hint Agent
    │
    ▼
Follow-Up Agent
    │
    ▼
Voice Interview Layer (LiveKit)
```

---

## 🤖 Multi-Agent System

### 🎤 Interviewer Agent
- Generates DSA interview questions
- Supports multiple topics
- Adaptive interview flow

### 📝 Evaluator Agent
- Evaluates candidate answers
- Reviews correctness
- Checks edge cases
- Analyzes time complexity
- Analyzes space complexity

### 💡 Hint Agent
- Provides progressive hints
- Prevents immediate solution leakage
- Encourages problem-solving

### 🔄 Follow-Up Agent
- Generates harder/easier variants
- Creates topic-specific follow-up questions
- Simulates real interviewer behavior

---

## 🎯 Features

### Technical Interview Simulation
- DSA Interview Questions
- Topic-Based Interviews
- Adaptive Questioning
- AI Evaluation

### Candidate Feedback
- Correctness Analysis
- Complexity Analysis
- Improvement Suggestions
- Interview Scoring

### Voice Interviewing
- Real-time Voice Interaction
- Speech-to-Text
- Text-to-Speech
- Interactive AI Conversations

### API-Driven Backend
- FastAPI REST APIs
- Swagger Documentation
- Modular Architecture

### Containerized Deployment
- Docker Support
- Portable Environment
- Easy Deployment

---

## 🛠️ Tech Stack

### AI & Agent Frameworks
- Agno
- OpenAI
- Groq

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Communication
- WebSockets
- HTTP APIs

### Voice AI
- LiveKit
- Deepgram
- ElevenLabs

### Python Ecosystem
- Python 3.11+
- Requests
- HTTPX
- AIOHTTP

### Logging & Monitoring
- Rich
- Loguru

### Testing
- Pytest

### Containerization
- Docker

### Environment Management
- Python Dotenv

---

## 📂 Project Structure

```text
ai-coding-interviewer/
│
├── agents/
│   ├── interviewer_agent.py
│   ├── evaluator_agent.py
│   ├── hint_agent.py
│   └── followup_agent.py
│
├── services/
│   ├── llm_service.py
│   └── interview_service.py
│
├── voice/
│   └── livekit_agent.py
│
├── utils/
│   ├── helpers.py
│   └── constants.py
│
├── .env
├── requirements.txt
├── Dockerfile
└── main.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-coding-interviewer.git

cd ai-coding-interviewer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key
DEEPGRAM_API_KEY=your_key
ELEVENLABS_API_KEY=your_key
```

---

## 🚀 Running Locally

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Deployment

Build Image:

```bash
docker build -t ai-interviewer .
```

Run Container:

```bash
docker run --env-file .env -p 8000:8000 ai-interviewer
```

---

## 📡 API Endpoints

### Start Interview

```http
GET /start
```

### Evaluate Answer

```http
POST /evaluate
```

### Generate Hint

```http
GET /hint
```

### Follow-Up Question

```http
GET /followup
```

---

## 🎓 Skills Demonstrated

### Artificial Intelligence
- Agentic AI Systems
- Multi-Agent Orchestration
- LLM Integration
- Prompt Engineering

### Backend Engineering
- REST APIs
- FastAPI Development
- Service-Oriented Architecture

### Software Engineering
- Modular Design
- Scalable Architecture
- Error Handling
- Testing

### DevOps
- Docker
- Environment Management
- Containerized Deployment

### Voice AI
- Real-Time Audio Processing
- Speech Recognition
- Text-To-Speech Systems

---

## 🚧 Future Enhancements

- Interview History Tracking
- Candidate Analytics Dashboard
- Weak Topic Detection
- Company-Specific Interview Modes
- Resume-Based Interviews
- Code Execution Sandbox
- AI Interview Reports
- Real-Time Collaborative Interviews

---

## 👨‍💻 Author

Built by a Computer Science student passionate about:

- Artificial Intelligence
- Agentic Systems
- Backend Engineering
- System Design
- Software Development

---

## ⭐ If you like this project

Give it a star and support the project!