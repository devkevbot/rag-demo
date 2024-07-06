# Retrieval-Augmented Generation Demo

## References

- https://learnbybuilding.ai/tutorials/rag-from-scratch
- https://learnbybuilding.ai/tutorials/rag-from-scratch-part-2-semantics-and-cosine-similarity
- https://github.com/ollama/ollama

## Overview

This repository contains three demo examples of retrieval-augmented generation (RAG).
Each demo shows an increasingly more sophisticated version of RAG, starting simple
and eventually using both embeddings and LLMs to generate an answer.

In each demo, we use RAG to suggest leisure activities for someone who likes to go hiking.

The following remains consistent across each demo:

- The user input: "I like to hike."
- The corpus of documents: `data/docs.json`.

## Installation

### Create a virtual environment

```sh
python -m venv .venv
source .venv/Scripts/activate
```

### Install the required Python packages

```sh
pip install -r requirements.txt
```

### Download and install Ollama

Ollama is used to run LLMs locally. Download it from [here](https://ollama.com/download).

## Run the demos

### Simple Demo

The demo can be run as follows:

```sh
python 1-demo-simple.py
```

### With LLM Demo

The demo can be run as follows:

First, start Ollama:

```sh
ollama serve
```

Then, in a new terminal:

```sh
# This may take a while
python 2-demo-with-llm.py
```

### With LLM and Embeddings Demo

The demo can be run as follows:

First, start Ollama:

```sh
ollama serve
```

Then, in a new terminal:

```sh
# This may take a while
python 3-demo-with-llm-and-embeddings.py
```
