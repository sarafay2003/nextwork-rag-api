from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
import ollama

app = FastAPI()

chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

class QueryRequest(BaseModel):
    q: str

@app.post("/query")
def query(req: QueryRequest):
    q = req.q

    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama.generate(
        model="tinyllama:latest",
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}
