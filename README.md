# 🔎 AI Reliability RAG

Baseline **AI Reliability** proof-of-concept.  
Focus: **making AI systems observable and reliable** — starting with simple retrieval, logs, and baseline metrics.  
This repo is part of my personal 6-week playbook toward **Platform AI-Ops / AI Reliability**.

---

## 🚀 What it does
- Ingest PDFs → chunk → embed → store in **Chroma** (vector DB)  
- Ask questions → retrieve top-K chunks by semantic similarity  
- Return **excerpts with citations** (no LLM yet)  
- Log per query: timestamp, latency, sources, answer length  

⚠️ This is **retrieval-only** (RA, no G). That’s intentional: first measure reliability signals, then add generation and controls later.

---

## 🛠 Quickstart

### Option A — Run locally
```bash
git clone https://github.com/naveedhsk/ai-reliability-rag.git
cd ai-reliability-rag

# Python 3.10+
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Put PDFs into ./data
mkdir data
cp ~/Downloads/*.pdf ./data/

# Ingest
python ingest.py --data_dir ./data --db ./chroma_db

# Ask questions
python ask_cli.py --db ./chroma_db --q "What are the four functions of the AI RMF?"

