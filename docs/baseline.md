# Week-1 AI Reliability — Baseline

## System
PDFs → chunk → embed (all-MiniLM-L6-v2) → Chroma → retrieve top-K → return excerpts + sources (CLI only).

## Metrics (from logs/interactions.csv)
- Queries: 10
- Latency p95: 0.45s
- No-citation rate: 10%
- Error rate: 0%

## Screenshots
![Example Q&A](../docs/screenshots/)  
![Metrics Summary](../docs/screenshots/rza1)

## Known issues
- Slow ingest for very large PDFs
- Occasional empty results
- No generation step yet


## Screenshots
![Example Q&A](../docs/screenshots/Screenshot - Answer for query-What are the characteristics of trustworthy AI in the NIST AI RMF?.png)  
![Metrics Summary](../docs/screenshots/metrics_table.png)

## Known issues
- PDF extraction sometimes noisy  
- Retrieval only, no LLM generation yet  
- Next: add SLOs + observability
