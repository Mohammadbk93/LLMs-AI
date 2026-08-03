#  Mohammad Bagheri — Applied AI Engineering Portfolio

> Building production-minded **LLM, RAG, and agentic systems** — from prompt evaluation pipelines to multi-agent workflows, vector search, and full-stack AI SaaS.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain" />
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Pinecone-000000?style=flat-square&logo=pinecone&logoColor=white" alt="Pinecone" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
</p>

---
##  Navigation

- [About](#-about)
- [Tech Stack](#-tech-stack)
- [Featured Projects](#-featured-projects)
  
---

## 👋 About

This repository is a curated portfolio of **applied AI engineering projects** spanning four themes:

- **Agentic & multi-agent workflows** — planning, reflection, and revision loops orchestrated with LangGraph and CrewAI.
- **Retrieval-Augmented Generation (RAG)** — semantic search over PDFs, SEC filings, and academic papers using Pinecone and ChromaDB.
- **LLM evaluation & prompt engineering** — structured, metric-driven testing with Promptfoo and LLM-as-a-judge.
- **Full-stack AI products** — shipped Streamlit apps and a production-grade SaaS captioning platform.

Each project pairs a working prototype with a clearly defined business use case.

---

## 🛠️ Tech Stack

| Category | Tools & Technologies |
|---|---|
| **Languages** | Python · TypeScript |
| **Agent & LLM Frameworks** | LangChain · LangGraph · CrewAI · n8n |
| **Models / Providers** | OpenAI (GPT-4o-mini, GPT-4.1-mini, TTS, Embeddings) · Anthropic Claude (Sonnet) · Google Gemini · Ollama (Llama 3.2) |
| **RAG & Vector DBs** | Pinecone · ChromaDB |
| **Search & Data APIs** | Tavily · SerpAPI · ArXiv API · SEC EDGAR · yfinance |
| **Evaluation** | Promptfoo · LLM-as-a-judge |
| **Frontend** | Streamlit · Next.js · Tailwind CSS |
| **Backend** | FastAPI · Celery · Redis |
| **Data & Parsing** | pandas · numpy · BeautifulSoup · PyPDF |
| **PDF Generation** | ReportLab · FPDF |
| **Infra & Automation** | Docker · Streamlit Cloud · Cloud Storage · Telegram Bot API · Google Drive |

---

##  Featured Projects

| # | Project | Focus | Live Demo |
|---|---|---|---|
| 1 | Prompt Engineering & Evaluation (Promptfoo) | LLM Evaluation | — |
| 2 | AI Document Q&A Agent (n8n) | RAG Automation | — |
| 3 | PhD Program Assistant | RAG Chatbot | [Open ↗](https://llms-phd-program.streamlit.app/) |
| 4 | AI Meal Planner Agent | Generative App | [Open ↗](https://aimealplanneragent.streamlit.app/) |
| 5 | Tweet Generator (Reflection Agents) | Agentic Workflow | [Open ↗](https://tweet-generator-langgraph.streamlit.app/) |
| 6 | Agentic Essay Writer | Multi-Agent | [Open ↗](https://agentic-essay-writer-k7.streamlit.app/) |
| 7 | AI Finance Agent | RAG + Market Intel | *Private* |
| 8 | AI Research Agent | RAG + Web Research | — |
| 9 | AI Interview Coach | Local LLM | *Private* |
| 10 | Smart Caption | Full-Stack SaaS | *Private beta* |
| 11 | Fine-Tuned Local Financial LLM | Fine Tuning for Finance | *Private* |


---

### 1. 🧪 Prompt Engineering & Evaluation — Promptfoo

<p align="center">
  <img src="https://github.com/user-attachments/assets/63838e5d-417b-4b34-94c1-486c3d80f222" alt="Promptfoo evaluation 1" width="24%" />
  <img src="https://github.com/user-attachments/assets/dc6894b7-6fcb-460a-b120-2933b1ab0952" alt="Promptfoo evaluation 2" width="24%" />
  <img src="https://github.com/user-attachments/assets/52a9d432-2b57-4b14-9609-554ff1f02b64" alt="Promptfoo evaluation 3" width="24%" />
  <img src="https://github.com/user-attachments/assets/36abc6f0-797b-468b-aada-ec42b55c003a" alt="Promptfoo evaluation 4" width="24%" />
</p>

Systematic, metric-driven testing of **four prompt strategies** — Standard, Emotional Stimuli, Expert Persona, and Zero-shot Chain-of-Thought — using **Promptfoo** with an LLM judge for semantic correctness.

- Dataset: **MMLU Astronomy** questions served from Google Sheets.
- Ran **1,824 individual test cases** with pass/fail metrics + semantic evaluation.
- Tracked **token usage, cost, and latency** across three models.

> **Multi-model run summary:** ~37 min · >1M tokens · ~$3.34 total

| Model | Cost |
|---|---|
| OpenAI (`gpt-4o-mini`) | $0.15 |
| Anthropic Claude (Sonnet) | $2.96 |
| Google Gemini (free tier) | $0.00 |

**Key takeaway:** automated evaluation pipelines — not intuition — are essential for scalable prompt engineering, and cost/latency must be actively managed across models.

**Stack:** Promptfoo · OpenAI `gpt-4o-mini` · Anthropic Claude (Sonnet) · Google Gemini · Node.js · Python · Google Sheets

---

### 2. 📄 AI Document Q&A Agent (n8n RAG)

<p align="center">
  <img src="https://github.com/user-attachments/assets/04e3f96b-8a85-46f9-98f1-e26d8d4d453a" alt="n8n RAG workflow" width="32%" />
  <img src="https://github.com/user-attachments/assets/008033d4-9564-4320-be20-11cc44a90a8f" alt="n8n RAG chat" width="32%" />
  <img src="https://github.com/user-attachments/assets/a3e96b88-0e91-4226-a72f-2e8f4056303c" alt="n8n RAG nodes" width="32%" />
</p>

A no-code/low-code **RAG system built entirely in n8n**: upload a PDF to Google Drive, then ask questions about its content and get grounded answers.

- Splits documents into chunks → embeds with OpenAI → stores in **Pinecone**.
- Retrieves the most relevant chunks per query and answers with **GPT-4o-mini**, using the document as the **only** source.
- Conversational Q&A through n8n's built-in chat interface.

**Use cases:** searchable internal docs, product-manual support bots, research-paper extraction, instant Q&A over course material.

**Stack:** n8n · OpenAI GPT-4o-mini + Embeddings · Pinecone · Google Drive

---

### 3. 🎓 PhD Program Assistant — RAG Chatbot

**[▶ Live App](https://llms-phd-program.streamlit.app/)**

![PhD Program Assistant — RAG Chatbot UI](https://github.com/user-attachments/assets/e35eed80-8a84-4225-b60b-928e3d78a49a)

A RAG chatbot that answers questions about PhD program details. PDFs are extracted with **PyPDF**, embedded via OpenAI, and stored in **Pinecone**; relevant context is retrieved at query time for accurate, context-aware responses instead of generic answers.

**Business value:** knowledge management, customer-support automation, education/training, and decision support over large document sets.

**Stack:** Python · Streamlit · OpenAI · Pinecone · PyPDF · dotenv

---

### 4. 🍽️ AI Meal Planner Agent

**[▶ Live App](https://aimealplanneragent.streamlit.app/)**

<p align="center">
  <img src="https://github.com/user-attachments/assets/23322977-2647-4e49-a86b-71271832a9a5" alt="AI Meal Planner — input view" width="48%" />
  <img src="https://github.com/user-attachments/assets/71fd7e60-feaa-4595-8975-7c2b6d824178" alt="AI Meal Planner — meal plan output" width="48%" />
</p>

Generates **personalized meal plans** from user-provided ingredients, calorie goals, and cooking styles.
- Download plans as **PDF** (ReportLab).
- **Voice-guided** cooking instructions via OpenAI Text-to-Speech.
- Breakfast, lunch, dinner, or full-day plans.

Combines AI-generated text, PDF generation, and voice synthesis into one interactive experience. *Planned: macro tracking, auth, saved history, multi-language, grocery lists.*

**Stack:** Streamlit · OpenAI GPT-4.1-mini + TTS · Python · ReportLab

---

### 5. 𝕏 Tweet Generator with Reflection Agents

**[▶ Live App](https://tweet-generator-langgraph.streamlit.app/)**

![Tweet Generator with Reflection Agents — Streamlit UI](https://github.com/user-attachments/assets/a4df0007-95de-47fb-9e10-de9878d2b224)

A **reflection-based agentic workflow** that iteratively improves its own output:

1. Generates an initial tweet
2. Critiques and reflects on it
3. Improves it across multiple drafts
4. Produces a final optimized version

Built on a **LangGraph** state machine with an interactive Streamlit UI.

**Stack:** Python · Streamlit · LangChain · LangGraph · OpenAI

---

### 6. ✍️ Agentic Essay Writer

**[▶ Live App](https://agentic-essay-writer-k7.streamlit.app/)**

![Agentic Essay Writer — Streamlit UI](https://github.com/user-attachments/assets/5022b38e-425d-4ac6-96be-59775f5d50d9)

A **multi-agent essay generation system** where specialized agents collaborate through a state-driven workflow — planning, web research, writing, critique, and revision — with **Tavily** web research and PDF export.

```text
User Input → Planner → Research → Writer → Reflection/Critique → Revision Research → Improved Essay → Final Output
```

**Core agents:** Planner (outline & flow) · Research (Tavily queries, factual grounding) · Writer (integrates outline + research + critique) · Reflection (identifies weaknesses, suggests revisions) · Revision loop (conditional graph routing).

**Stack:** LangGraph · LangChain · OpenAI · Tavily · Streamlit · FPDF

---

### 7.  AI Finance Agent

> ⚠️ **Private research project.** Built for learning and experimentation with AI-driven financial analysis. Professional trading requires strict risk management and validated strategies, so this is intentionally evolving as the underlying financial logic is refined.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9d0d4083-450b-4a57-9b8a-d7d5cd887110" alt="AI Finance Agent — dashboard" width="48%" />
  <img src="https://github.com/user-attachments/assets/29a58d7a-73c9-49e2-a987-8aa7d507ae65" alt="AI Finance Agent — sector view" width="48%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/87847920-bcf1-4f3c-9840-490a59311f1f" alt="AI Finance Agent — opportunity scoring" width="48%" />
  <img src="https://github.com/user-attachments/assets/e72bba68-3890-49f9-b8ee-71400285a53c" alt="AI Finance Agent — company drilldown" width="48%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/216d84e9-8d93-49c6-a0b4-cd02e87a9ec2" alt="AI Finance Agent — SEC RAG analysis" width="48%" />
  <img src="https://github.com/user-attachments/assets/55caa395-51ac-41ab-aa06-ae39b782162f" alt="AI Finance Agent — news sentiment" width="48%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/fe5e9633-7ea5-45ca-bee3-e348b4eaabc2" alt="AI Finance Agent — research chat" width="98%" />
</p>

An AI-powered **market scanning and research platform** that analyzes stocks, sectors, trends, news sentiment, SEC filings, and fundamentals to surface potential opportunities across the US market.

- **SEC Filing RAG** — downloads & indexes 10-K filings into **ChromaDB** for semantic search.
- **S&P 500 + Sector scanners** — ranks sectors (Tech, Healthcare, Energy, etc.) by average opportunity score.
- **Opportunity Scoring Engine** — combines revenue/earnings growth, trend & momentum, news sentiment, profitability, valuation, and debt.
- **Telegram alerts** for high-confidence opportunities + historical scan tracking.
- Interactive Streamlit dashboard with an AI research chat.

```text
S&P 500 Companies → Market Data → Trend + Fundamentals → News Sentiment
→ Opportunity Scoring → Sector Classification → AI + SEC RAG → Telegram Alerts
```

*Planned: SerpAPI integration for real-time market data.*

**Stack:** Python · Streamlit · OpenAI · ChromaDB · LangGraph · LangChain · yfinance · pandas · numpy · BeautifulSoup · Telegram Bot API · dotenv

---

### 8. 🔎 AI Research Agent

<p align="center">
  <img src="https://github.com/user-attachments/assets/a5136da4-ab60-4072-9e13-9f8b7e3aa8c3" alt="AI Research Agent — report output" width="32%" />
  <img src="https://github.com/user-attachments/assets/de61cda4-f27e-4fc4-a7dd-578863c35b91" alt="AI Research Agent — query interface" width="32%" />
  <img src="https://github.com/user-attachments/assets/c57f7459-0f33-4840-8b2b-50524dcf1f7c" alt="AI Research Agent — sources" width="32%" />
</p>

A **LangGraph-powered research assistant** that produces structured research reports by combining ArXiv ingestion, web search, and a RAG pipeline. An Oracle/Router decides between three tools per query.

```text
                    ┌─────────────────────┐
                    │    User Question    │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ LangGraph Workflow  │
                    │   Oracle + Router   │
                    └──────────┬──────────┘
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
 ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
 │  rag_search  │     │ fetch_arxiv  │     │  web_search  │
 └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
        ▼                    ▼                    ▼
 ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
 │  Pinecone DB │    │    ArXiv     │    │   SerpAPI    │
 └──────┬───────┘    └──────────────┘    └──────────────┘
        ▼
 ┌─────────────────────┐
 │   final_answer →    │
 │  Structured Report  │
 └─────────────────────┘
```

**Ingestion pipeline:** ArXiv API → download PDFs → load → split into chunks → OpenAI embeddings → Pinecone → used by RAG search tools.

**Stack:** Python · LangGraph · LangChain · OpenAI · Pinecone · Streamlit · SerpAPI · ArXiv API

---

### 9. 🧑‍💻 AI Interview Coach

> 🔒 Private project under active development.

<p align="center">
  <img src="https://github.com/user-attachments/assets/45c519d4-2d34-4cc1-b4b2-687b12eda906" alt="AI Interview Coach — home" width="48%" />
  <img src="https://github.com/user-attachments/assets/b093c9c5-d84b-4665-baa2-37b33d5e26a2" alt="AI Interview Coach — study material" width="48%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/81ec1845-0778-4625-a47e-272335c2d721" alt="AI Interview Coach — question generation" width="48%" />
  <img src="https://github.com/user-attachments/assets/b89e1deb-dacc-4ed4-8d9f-1d8cc31307dd" alt="AI Interview Coach — interview session" width="48%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/f79e0b72-0bf8-4f45-8c5c-768245c1c955" alt="AI Interview Coach — evaluation" width="48%" />
  <img src="https://github.com/user-attachments/assets/785f1f95-2dd1-4449-b0b9-ceb0b91cea70" alt="AI Interview Coach — study plan" width="48%" />
</p>

A **fully local** interview-prep platform for junior and mid-level developers, designed to keep data private and avoid cloud costs.

- AI-generated study material and dynamic technical questions.
- Automated answer evaluation with strengths/weaknesses feedback.
- **7-day study plans**, multiple difficulty levels, and multi-language support.
- Runs locally on **Ollama + CrewAI** (Llama 3.2).

**Topics supported:** Python · FastAPI · ML · DL · AI · Data Science · MLOps · LLMOps · AIOps

**Stack:** Python · Streamlit · CrewAI · Ollama · Llama 3.2

---

### 10. 🎬 Smart Caption — AI Video Captioning & Translation

> 🚧 Under active development · private beta.

https://github.com/user-attachments/assets/a4b7c02b-8fc6-447b-89c3-035de0c4f3e9

A modern **full-stack SaaS** platform that generates high-quality subtitles in **99+ languages** and exports videos with permanently embedded captions.

- Automatic speech-to-text transcription + multi-language translation.
- Custom subtitle styling and positioning, with **LTR and RTL** support.
- Fast cloud-based processing, secure auth, usage tracking, and an admin analytics dashboard.

*Roadmap: subscription/billing, mobile apps, advanced subtitle editing, preset styling templates.*

**Stack:** Next.js · TypeScript · Tailwind CSS · FastAPI · Celery · Redis · Docker · Cloud Storage

---

<p align="center"><i>Each project is a working prototype paired with a clear, real-world use case.</i></p>

---

### 11. Local Financial LLM — Fine-Tuned Qwen2.5-3B.
<img width="342" height="64" alt="image" src="https://github.com/user-attachments/assets/d9315bfc-767f-4e5d-a229-ac2f1a53d0fa" />

A domain-specialized financial language model built end-to-end on free infrastructure:
trained on Google Colab (T4 GPU) using LoRA fine-tuning, and served locally on Apple
Silicon via MLX-LM.

## What it does
- Financial sentiment classification (Bullish / Bearish / Neutral)
- Gold-macro reasoning (DXY, real yields, CPI, central bank dynamics)
- Ticker and entity extraction from earnings calls and news headlines

## Stack
`Qwen2.5-3B-Instruct` · `LoRA (r=16, α=32)` · `Unsloth` · `TRL 0.24.0` · `MLX-LM` · 

## Current Limitations & Roadmap
> ⚠️ This is a proof-of-concept trained on 30 synthetic samples — intentionally minimal
> to demonstrate the full pipeline on free-tier infrastructure.

Real production quality requires:
- **500–5,000+ samples** of real financial news, earnings transcripts, and macro data
- **Stronger infrastructure** — a paid Colab Pro+ session, a cloud GPU (A100/H100),
  or a dedicated on-premise server to handle larger datasets and longer training runs
- **Longer training** — 10–20 epochs on a diverse, high-quality dataset

The architecture is fully production-ready and horizontally scalable — swapping in a
larger dataset and more compute is the only step between this prototype and a
deployment-grade financial NLP model.

## Deployment paths
| Target | Tool | Status |
|---|---|---|
| Apple Silicon (M-series) | MLX-LM | ✅ Working |
| Local API for LangGraph agent | `mlx_lm.server` on port 8080 | ✅ Working |
| HuggingFace Hub | Safetensors (float16) | ✅ Uploaded |

## GGUF Conversion
The merged model can be converted to GGUF format (Q4_K_M quantization) for:
- **Ollama** — serving on enterprise Linux servers or any OS without Python dependencies
- **llama.cpp** — CPU inference on edge devices and air-gapped environments
- **LM Studio / Jan.ai** — non-technical user interfaces for local LLM interaction
- **Docker deployment** — single portable `.gguf` file, no environment setup required
- **Team distribution** — one file shared across the team, pulled directly via
  `ollama run hf.co/mohammadbk321/financial-qwen-3b-GGUF`
