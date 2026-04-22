# AI Form Architect

A responsive, AI-powered form generator using **Google Gemini** (Cloud) and **Ollama** (Local). This application is built with **FastAPI** on the backend and plain HTML/Tailwind CSS on the frontend.

## Features
- Generate a sleek modern UI from text descriptions.
- Use either Local AI Models via Ollama (secure, offline) or Google Gemini (powerful, fast).
- Copy the generated beautiful HTML code instantly.
- Glassmorphism & Responsive Tailwind CSS layout.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com/) (Optional: if you want to use local models)

### 2. Installation Setup
Clone the repository, then install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Rename `.env.example` to `.env` and put your Gemini API Key:
```env
GEMINI_API_KEY=your_actual_key_here
```

### 4. Running the Project
**Terminal 1 (Backend API):**
```bash
uvicorn main:app --reload
```
The API will run at `http://127.0.0.1:8000`.

**Terminal 2/Browser (Frontend UI):**
You can simply double click `index.html` to run it in your browser directly, or serve it using an extension like Live Server in VS Code.

## 🤖 Models Supported
- Local: All Ollama models installed on your machine (`llama3`, `mistral`, `phi3`, etc)
- Cloud: default falls back to `gemini-2.5-flash` but allows selecting specific ones if configured.