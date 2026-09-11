import os
import signal
import sys
from dotenv import load_dotenv

load_dotenv()

from google import genai
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_rag_prompt(query, context):
    escaped = context.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""
You are a helpful and informative bot that answers questions using text from the reference context included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and conversational tone. \
  If the context is irrelevant to the answer, you may ignore it.
                QUESTION: '{query}'
                CONTEXT: '{context}'
              
              ANSWER:
              """).format(query=query, context=context)
    return prompt


def get_relevant_context_from_db(query):
    context = ""
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./chroma_db_nccn", embedding_function=embedding_function)
    search_results = vector_db.similarity_search(query, k=6)
    for result in search_results:
        context += result.page_content + "\n"
    return context


def generate_answer(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text


def ask(query):
    """Full RAG pipeline: query -> context -> prompt -> answer."""
    context = get_relevant_context_from_db(query)
    prompt = generate_rag_prompt(query=query, context=context)
    return generate_answer(prompt=prompt)


# --- CLI mode (only runs when executed directly) ---
if __name__ == "__main__":
    def signal_handler(sig, frame):
        print('\nThanks for using Gemini. :)')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    welcome_text = generate_answer("Can you quickly introduce yourself")
    print(welcome_text)

    while True:
        print("-----------------------------------------------------------------------\n")
        print("What would you like to ask?")
        query = input("Query: ")
        answer = ask(query)
        print(answer)