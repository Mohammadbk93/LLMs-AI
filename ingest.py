import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone
from pypdf import PdfReader

# ---- LOAD ENV ----
load_dotenv(dotenv_path=".env")

# ---- INIT CLIENTS ----
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index(os.getenv("PINECONE_INDEX"))


# ---- LOAD PDF ----
def load_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:  # avoid NoneType error
            text += extracted + "\n"

    return text


# ---- CHUNK TEXT ----
def chunk_text(text, size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap

    return chunks


# ---- EMBEDDING ----
def get_embedding(text):
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return res.data[0].embedding


# ---- INGEST PIPELINE ----
def ingest(file_path):
    print("📄 Reading file...")
    text = load_pdf(file_path)

    if not text.strip():
        print("⚠️ No text extracted from PDF")
        return

    print("✂️ Chunking...")
    chunks = chunk_text(text)

    print(f"Chunks: {len(chunks)}")

    vectors = []

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)

        vectors.append({
            "id": f"chunk-{i}",
            "values": embedding,
            "metadata": {"text": chunk}
        })

        # batch upload
        if len(vectors) >= 50:
            index.upsert(vectors)
            vectors = []

    # upload remaining
    if vectors:
        index.upsert(vectors)

    print("✅ Done uploading!")


# ---- RUN ----
if __name__ == "__main__":
    ingest("data/PNRR_2_PhD Programme.pdf")