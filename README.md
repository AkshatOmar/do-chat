# 🤖 DoChat — AI Document Chat

> Chat with any PDF using natural language. Powered by Google Gemini AI + RAG (Retrieval-Augmented Generation).

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini%202.0%20Flash-orange?logo=google)](https://ai.google.dev)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-purple)](https://www.trychroma.com)

---

## 🌟 What is DoChat?

DoChat is a web app that lets you **upload a PDF and ask it anything** in plain English. It uses a technique called **RAG (Retrieval-Augmented Generation)** to find the most relevant parts of your document and pass them to Google Gemini AI, which then gives you a clear, conversational answer.

No hallucinations — the AI only answers from your actual document content.

---

## ✨ Features

- 💬 **Natural language Q&A** — ask questions about your PDF in plain English
- 🎨 **Beautiful dark UI** — glassmorphism design with smooth animations
- ⚡ **Typing indicator** — animated dots while the AI is thinking
- 📋 **Copy button** — copy any answer with one click
- 💡 **Suggested questions** — quick-start prompts in the sidebar
- 📄 **Document stats** — shows indexed chunk count, model info, live status
- 🔒 **Secure** — API key stored in environment variable, never in code

---

## 🏗️ How It Works

```
Your PDF
   │
   ▼
[generate_embeddings.py]
   │  Split into chunks (1000 chars, 100 overlap)
   │  Embed each chunk using sentence-transformers/all-MiniLM-L6-v2
   ▼
ChromaDB (local vector database)
   │
   │  User types a question
   ▼
Find top 6 most relevant chunks (similarity search)
   │
   ▼
Build prompt = Question + Retrieved Context
   │
   ▼
Google Gemini 2.0 Flash
   │
   ▼
Friendly, accurate answer shown in the chat UI
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Google Gemini 2.0 Flash |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` (runs locally) |
| **Vector Database** | ChromaDB (persisted to disk) |
| **Backend** | Python + Flask |
| **Frontend** | Vanilla HTML / CSS / JavaScript |
| **Orchestration** | LangChain |

---

## 🚀 Local Setup

### Prerequisites
- Python 3.11+
- A [Google Gemini API key](https://ai.google.dev/gemini-api/docs/api-key) (free)

### Steps

1. **Clone the repo**
   ```bash
   git clone https://github.com/AkshatOmar/do-chat.git
   cd do-chat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   # source venv/bin/activate # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key** — create a `.env` file:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **(First time only) Index your PDF**
   ```bash
   python generate_embeddings.py
   ```
   > This reads `report.pdf`, splits it into chunks, and saves embeddings to `chroma_db_nccn/`

6. **Run the web app**
   ```bash
   python app.py
   ```

7. **Open your browser** → [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
do-chat/
├── app.py                  # Flask backend (REST API)
├── rag.py                  # RAG pipeline (query → context → answer)
├── generate_embeddings.py  # One-time PDF indexing script
├── report.pdf              # Source PDF document
├── chroma_db_nccn/         # Persisted vector database
├── templates/
│   └── index.html          # Chat UI (HTML/CSS/JS)
├── requirements.txt        # Python dependencies
├── Procfile                # For Render/Railway deployment
├── runtime.txt             # Python version pin
└── .env                    # API key (not committed to git)
```

---

## ☁️ Deploy on Render (Free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your `do-chat` GitHub repo
4. Fill in:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `python app.py`
5. Add **Environment Variable**:
   - Key: `GEMINI_API_KEY`
   - Value: your Gemini API key
6. Click **Deploy** — get a public URL like `https://do-chat.onrender.com` 🎉

---

## 🔄 Using a Different PDF

1. Replace `report.pdf` with your PDF
2. Delete the `chroma_db_nccn/` folder
3. Re-run `python generate_embeddings.py`
4. Start the app normally

---

## 📄 License

MIT — free to use, modify, and share.
