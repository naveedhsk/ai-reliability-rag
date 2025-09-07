import os, argparse, time, chromadb, csv
from sentence_transformers import SentenceTransformer
from datetime import datetime

def log_row(path, row):
    ex = os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts","query","top_sources","latency_s","answer_len","model","usage_tokens"])
        if not ex: w.writeheader()
        w.writerow(row)

def main(db_path, collection, query, top_k):
    client = chromadb.PersistentClient(path=db_path)
    coll = client.get_or_create_collection(name=collection)
    embed = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    q_emb = embed.encode([query], normalize_embeddings=True).tolist()
    t0 = time.time()
    res = coll.query(query_embeddings=q_emb, n_results=top_k, include=["documents","metadatas"])
    latency = time.time() - t0

    docs = res["documents"][0] if res["documents"] else []
    metas = res["metadatas"][0] if res["metadatas"] else []
    pairs = [(os.path.basename(m.get("source","")), m.get("page","?"), d) for d,m in zip(docs,metas)]

    if not pairs:
        answer = "No relevant excerpts found."
        top_sources = ""
    else:
        answer = "Top relevant excerpts:\n" + "\n\n".join([f"- ({s}:{p}) {d[:500]}..." for s,p,d in pairs])
        top_sources = ";".join([f"{s}:{p}" for s,p,_ in pairs])

    print("\n=== ANSWER ===\n", answer, "\n")
    print("=== SOURCES ===")
    [print(f"- {s} (p.{p})") for s,p,_ in pairs]

    os.makedirs("./logs", exist_ok=True)
    log_row("./logs/interactions.csv", {
        "ts": datetime.utcnow().isoformat(),
        "query": query,
        "top_sources": top_sources,
        "latency_s": round(latency,3),
        "answer_len": len(answer),
        "model": "extractive",
        "usage_tokens": ""
    })

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="./chroma_db")
    ap.add_argument("--collection", default="docs")
    ap.add_argument("--q", required=True)
    ap.add_argument("--k", type=int, default=4)
    a = ap.parse_args()
    main(a.db, a.collection, a.q, a.k)
