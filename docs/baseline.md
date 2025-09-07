# Week-1 AI Reliability — Baseline

## System
PDFs → chunk → embed (all-MiniLM-L6-v2) → Chroma → retrieve top-K → return excerpts + sources (CLI only).

## Metrics (from logs/interactions.csv)
- Queries: 10
- Latency p95: 0.45s
- No-citation rate: 10%
- Error rate: 0%

## Screenshots
1. CLI Q&A output
2. Another query
3. Metrics table

## Known issues
- Slow ingest for very large PDFs
- Occasional empty results
- No generation step yet
