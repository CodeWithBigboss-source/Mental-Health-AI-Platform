# Mental Health AI Platform

An AI-powered mental-health support platform: text chat with safety-aware
responses, mood tracking, and guided wellness exercises. Built in three
independent modules — AI engine, backend, and frontend.

**Not a replacement for professional mental-health care.** If you are in
immediate danger, contact your local emergency services.

---

## Project Structure

```
mental-health-ai-platform/
├── ai-engine/    # Core AI logic: LLM, safety classifier, memory, RAG, PII detection
├── backend/      # FastAPI server: auth, chat/mood/exercise endpoints, voice STT/TTS
└── frontend/     # Next.js web app
```

Each of `ai-engine/` and `backend/` has its **own Python virtual environment**.
`frontend/` uses Node/npm. They must be run as three separate, simultaneous processes.

---

## First-Time Setup (do this once)

### 1. Prerequisites

- Python 3.11+
- Node.js 18+
- A [Groq](https://console.groq.com) API key
- A [Supabase](https://supabase.com) project (with the `documents`, `users`,
  `conversations`, `messages`, `mood_entries` tables and the `match_documents`
  function already created — see project setup notes)

### 2. AI Engine setup

```powershell
cd "E:\Mental Health AI\mental-health-ai-platform\ai-engine"
python -m venv venv
venv\Scripts\activate
pip install -e .
python -m spacy download en_core_web_lg
```

Create `ai-engine/.env`:

```
GROQ_API_KEY=your_groq_key_here
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_service_role_key
```

Seed the RAG knowledge base (one-time):

```powershell
python -m ai_engine.rag.seed_data
```

Verify it works:

```powershell
python -m ai_engine.evaluation.run_eval
```

### 3. Backend setup

```powershell
cd "E:\Mental Health AI\mental-health-ai-platform\backend"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `backend/.env`:

```
GROQ_API_KEY=your_groq_key_here
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_service_role_key
JWT_SECRET=generate_a_random_long_string_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

### 4. Frontend setup

```powershell
cd "E:\Mental Health AI\mental-health-ai-platform\frontend"
npm install
```

Create `frontend/.env.local`:

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

Setup is done. Move to **Daily Use** below every time you come back to work on this.

---

## Daily Use (every time you want to run the project)

You need **two terminals** open at the same time.

### Terminal 1 — Backend

```powershell
cd "E:\Mental Health AI\mental-health-ai-platform\backend"
venv\Scripts\activate
uvicorn app.main:app --reload --reload-dir app
```

Wait for `Application startup complete` (can take up to ~30–50 seconds the
first time, due to loading the PII/embedding models — this is normal).

### Terminal 2 — Frontend

```powershell
cd "E:\Mental Health AI\mental-health-ai-platform\frontend"
npm run dev
```

Then open: **http://localhost:3000**

### Stopping everything

`Ctrl + C` in each terminal.

### Backend API docs (for testing endpoints directly)

http://127.0.0.1:8000/docs

---

## Running AI Engine Scripts Directly (optional, for testing/debugging)

```powershell
cd "E:\Mental Health AI\mental-health-ai-platform\ai-engine"
venv\Scripts\activate
python -m ai_engine.evaluation.run_eval
```

Always use `python -m ai_engine.<path>`, never run `.py` files directly by
path — the `-m` flag is required for internal imports to resolve.

---

## Tech Stack

- **AI Engine:** Groq (LLM + Whisper STT + Orpheus TTS), sentence-transformers, Presidio (PII detection)
- **Backend:** FastAPI, Supabase/PostgreSQL + pgvector, JWT auth, slowapi (rate limiting)
- **Frontend:** Next.js (App Router), TypeScript, Tailwind CSS, Framer Motion, Zustand

## Safety Design

Every chat message is classified on a 0–4 risk scale before a response is
generated. Level 4 (crisis-level language) bypasses normal AI generation
entirely and returns a fixed safety response with crisis resources — this
behavior is covered by an automated eval suite (`ai_engine/evaluation/`) run
before any change to the safety layer.

Regards:
MALIK AHSAN NASAR
[LINKEDIN](https://www.linkedin.com/in/malikahsannasar/)
