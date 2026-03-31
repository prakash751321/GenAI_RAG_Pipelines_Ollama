# GenAI RAG Pipeline with Ollama

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline using LLMs and vector search to provide context-aware responses.

## Features
- Document ingestion
- Chunking strategy
- Embeddings + vector storage
- Semantic retrieval
- LLM response generation

## Tech Stack
- Python
- LangChain
- Ollama
- FAISS (or your DB)

## How it works
1. Load documents
2. Split into chunks
3. Generate embeddings
4. Store in vector DB
5. Retrieve top-k context
6. Pass to LLM

## Run locally
```bash
pip install -r requirements.txt
python simplerag.py
python chunks_in_rag.py
