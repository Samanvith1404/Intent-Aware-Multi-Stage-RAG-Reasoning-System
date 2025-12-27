# Intent-Aware Multi-Stage RAG Reasoning System

This project implements an applied AI system that extends standard Retrieval-Augmented Generation (RAG) by introducing intent-aware routing and multi-stage reasoning. Instead of producing single-pass answers, the system adapts its reasoning depth based on user intent and provides structured, evidence-grounded guidance for idea evaluation, research prompts, hackathon concepts, and general queries.

The goal of this project is to demonstrate how RAG systems can be designed as decision-support pipelines rather than simple conversational agents.

---

## Problem Statement

Most RAG implementations follow a basic pattern: retrieve context and generate a response. While effective for factual queries, this approach fails for evaluation-heavy tasks that require balanced reasoning, trade-off analysis, and clear guidance.

This project addresses those limitations by:
- detecting user intent before reasoning,
- separating reasoning into focused stages,
- and synthesizing conclusions grounded in retrieved evidence.

---

## System Overview

The system operates in two modes, selected dynamically:

1. Normal Flow for low-complexity queries  
2. Reasoning Flow for high-complexity evaluation tasks  

A routing LLM determines which path to execute based on the user prompt.

---

## Routing Logic

Each user prompt is classified into one of the following categories:

- research  
- idea_evaluation  
- hackathon  
- others  

Prompts classified as `others` follow a lightweight response path. Prompts in the remaining categories trigger the multi-stage reasoning pipeline. This design balances reasoning depth with cost and latency.

---

## Normal Flow

The normal flow is used for general informational queries that do not require structured evaluation.

In this mode, the system:
- retrieves a small set of relevant documents,
- generates a single response grounded in that context.

This path prioritizes simplicity and efficiency.

---

## Reasoning Flow

The reasoning flow is activated for research, idea evaluation, and hackathon-related prompts.

In this mode, the system:
1. Retrieves relevant documents using hybrid retrieval.
2. Extracts positive aspects using a dedicated reasoning prompt.
3. Extracts negative aspects using a separate reasoning prompt.
4. Synthesizes both perspectives into a structured conclusion with guidance.

Separating positives and negatives enforces balanced reasoning and reduces bias.

---

## Key Design Decisions

- Intent-aware routing ensures reasoning depth matches query complexity.
- Hybrid retrieval improves grounding and contextual relevance.
- Separate reasoning paths enforce analytical discipline.
- Final synthesis focuses on guidance and next steps, not just summarization.

These design choices reflect applied AI system patterns rather than experimental chatbots.

---

## Project Structure

intent-aware-multistage-rag/
├── main.py
├── router/
├── retrieval/
├── reasoning/
├── normal/
├── config/
└── requirements.txt


Each module represents a distinct responsibility within the pipeline.

---

## Example Use Case

User prompt:  
"I have an idea for an AI-based healthcare hackathon project. Is it feasible?"

System behavior:
- The router classifies the prompt as hackathon-related.
- Relevant contextual documents are retrieved.
- Positive and negative aspects are analyzed independently.
- A final response provides feasibility analysis and suggested next steps.

---

## Limitations

- Output quality depends on the availability and relevance of retrieved documents.
- Router misclassification can affect reasoning depth.
- Multi-stage reasoning increases cost compared to single-pass RAG.
- No automated evaluation metrics are included.

These limitations are intentionally documented.

---

## Future Improvements

- Confidence scoring for reasoning outputs
- Citation tracking for retrieved evidence
- Router fallback strategies
- Parallel execution of reasoning stages

---

## Intended Use

This project is intended to demonstrate:
- applied RAG system design,
- LLM orchestration and routing,
- structured reasoning over retrieved context.

It is designed as a portfolio project for Applied AI and LLM-focused roles and is not positioned as a production-ready system.

---

## Tech Stack

- Python  
- LLM APIs (Groq / OpenAI-compatible)  
- Hybrid retrieval mechanisms  
- Modular prompt design  

---

## License

This project is intended for educational and portfolio use.
