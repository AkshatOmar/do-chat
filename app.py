import os
from flask import Flask, request, jsonify, render_template
from rag import ask, get_relevant_context_from_db
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

app = Flask(__name__)

PDF_NAME = "Best Buy FY2023 Annual Report"
APP_NAME = "DoChat"

def get_doc_count():
    try:
        embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_db = Chroma(persist_directory="./chroma_db_nccn", embedding_function=embedding_function)
        return vector_db._collection.count()
    except Exception:
        return "Unknown"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():
    return jsonify({
        "pdf_name": PDF_NAME,
        "doc_count": get_doc_count(),
        "status": "ready"
    })


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query cannot be empty"}), 400
    try:
        answer = ask(query)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting RAG Web Platform...")
    print("Loaded:", PDF_NAME)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
