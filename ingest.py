import os, argparse, uuid, chromadb
from sentence_transformers import SentenceTransformer
from util import load_pdfs, chunk_text

def main(data_dir, db_path, collection="docs", chunk_size=1000, overlap=200, batch=64):
    os.makedirs(db_path, exist_ok=True)
    client = chromadb.PersistentClient(path=db_path)
    coll = client.get_or_create_collection(name=collection)
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    pages = load_pdfs(data_dir)
    if not pages:
        print("No PDFs found in", data_dir)
        return

    texts, metas, ids = [], [], []
    for (src, pg, txt) in pages:
        for i, ch in enumerate(chunk_text(txt, chunk_size, overlap)):
            texts.append(ch)
            metas.append({"source": src, "page": pg})
            ids.append(f"{uuid.uuid4().hex}_{pg}_{i}")
            if len(texts) >= batch:
                embs = model.encode(texts, normalize_embeddings=True).tolist()
                coll.add(documents=texts, metadatas=metas, embeddings=embs, ids=ids)
                texts, metas, ids = [], [], []
    if texts:
        embs = model.encode(texts, normalize_embeddings=True).tolist()
        coll.add(documents=texts, metadatas=metas, embeddings=embs, ids=ids)

    print(f"✅ Ingest complete. Count={coll.count()} | DB={db_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir", required=True)
    ap.add_argument("--db", default="./chroma_db")
    ap.add_argument("--collection", default="docs")
    ap.add_argument("--chunk_size", type=int, default=1000)
    ap.add_argument("--overlap", type=int, default=200)
    a = ap.parse_args()
    main(a.data_dir, a.db, a.collection, a.chunk_size, a.overlap)
