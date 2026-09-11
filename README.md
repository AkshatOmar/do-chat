# DoChat — AI Document Chat

A RAG (Retrieval-Augmented Generation) web platform that lets you chat with any PDF using Google Gemini AI.

## Features
- Beautiful dark glassmorphism chat UI
- Powered by Google Gemini Flash + ChromaDB + HuggingFace Embeddings
- Ask natural language questions about your PDF
- Animated typing indicator, copy buttons, suggested questions

## Tech Stack
- **LLM**: Google Gemini 2.0 Flash
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (local)
- **Vector DB**: ChromaDB (local, persisted)
- **Backend**: Flask
- **Frontend**: Vanilla HTML/CSS/JS

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/YOUR_USERNAME/pdf-insight.git
   cd pdf-insight
   ```

2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Gemini API key
   ```
   GEMINI_API_KEY=your_key_here
   ```

4. (First time only) Generate embeddings from your PDF
   ```bash
   python generate_embeddings.py
   ```

5. Run the web app
   ```bash
   python app.py
   ```

6. Open [http://localhost:5000](http://localhost:5000)

## Deploying to Render (free)
1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set environment variable: `GEMINI_API_KEY`
5. Build command: `pip install -r requirements.txt`
6. Start command: `python app.py`
