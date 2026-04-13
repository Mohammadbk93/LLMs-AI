import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

# Load env
load_dotenv(dotenv_path=".env")

# Init clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index(os.getenv("PINECONE_INDEX"))


# ---- EMBEDDING ----
def get_embedding(text):
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return res.data[0].embedding


# ---- RAG PIPELINE ----
def ask_rag(question):
    # Step 1: Embed question
    query_embedding = get_embedding(question)

    # Step 2: Search Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )

    # Step 3: Build context
    context = "\n".join(
        [match["metadata"]["text"] for match in results["matches"]]
    )

    print("----- CONTEXT -----")
    print(context[:500])

    # Step 4: Generate answer
    prompt = f"""
You are a helpful AI assistant.

Use the context below to answer the question.

- If the answer is clearly in the context → answer accurately.
- If partially relevant → explain using context.
- If not relevant → answer using general knowledge.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content