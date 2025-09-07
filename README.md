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

```

### Option B — Run in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/naveedhsk/ai-reliability-rag/blob/main/notebooks/demo.ipynb)

```bash
📊 Week-1 Baseline Metrics

Queries: 10

Latency p95: 0.45s

No-citation rate: 10%

Error rate: 0%

Example output
Q: What are the four functions of the AI RMF?

=== ANSWER ===
Top relevant excerpts:
- (nist.ai.100-1.pdf:12) Map, Measure, Manage, Govern are the four core functions...

=== SOURCES ===
- nist.ai.100-1.pdf (p.12)
```

📂 Structure
.
├── ingest.py         # Ingest PDFs → Chroma
├── ask_cli.py        # Query & log answers
├── util.py           # PDF loader + chunker
├── requirements.txt
├── data/             # Place PDFs here (not tracked)
├── logs/             # Auto-created query logs
└── docs/             # Metrics, screenshots, write-ups

## 📅 Roadmap

Week-1: ✅ Baseline retrieval + metrics

Week-2: Add SLOs + runbook + observability

Week-3: Eval harness (factuality, refusals, prompt-injection probes)

Week-4: Cost-per-answer lens (FinOps Lite)

Week-5: 5 pragmatic controls (Governance Lite)

Week-6: Incident drill + final report

## ✍️ Author

Built by Naveedh SK
Exploring AI Reliability / Platform AI-Ops
Follow the journey → LinkedIn https://www.linkedin.com/in/naveedh-sk/


