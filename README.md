# Applied Prompt Engineering: Prompt Testing and Evaluation with Promptfoo

<p align="center">
  <img src="https://github.com/user-attachments/assets/63838e5d-417b-4b34-94c1-486c3d80f222" width="23%" />
  <img src="https://github.com/user-attachments/assets/dc6894b7-6fcb-460a-b120-2933b1ab0952" width="23%" />
  <img src="https://github.com/user-attachments/assets/52a9d432-2b57-4b14-9609-554ff1f02b64" width="23%" />
  <img src="https://github.com/user-attachments/assets/36abc6f0-797b-468b-aada-ec42b55c003a" width="23%" />
</p>

## What I Have Done
In this project, I explored and evaluated different prompt engineering techniques using Promptfoo. I designed and tested four types of prompts:

1. Standard Prompt  
2. Emotional Stimuli Prompt  
3. Expert Persona Prompt  
4. Zero-shot Chain-of-Thought (CoT) Prompt  

The evaluation was conducted using the OpenAI model (`gpt-4o-mini`) as both the response generator and LLM judge. I used a dataset of structured questions (MMLU Astronomy) stored in a Google Sheet and integrated it into Promptfoo for automated testing.

The experiment included:
- Running prompt evaluations across multiple test cases  
- Comparing prompt performance using pass/fail metrics  
- Using an LLM-based judge for semantic evaluation  
- Tracking token usage, cost, and execution time  

In total, I ran 1824 individual test cases including evaluation by an LLM judge.

---
## Why It Is Important

Prompt engineering plays a critical role in improving the quality and reliability of LLM outputs. This project demonstrates:

- How different prompt strategies impact model performance  
- The importance of structured evaluation instead of intuition  
- The use of LLM-as-a-judge for semantic correctness  
- Trade-offs between cost, latency, and accuracy when scaling across models  

Additionally, testing across multiple models significantly increases both cost and runtime. For example:

- Total duration (3 models): ~37 minutes  
- Total tokens: >1 million  
- Total cost: ~$3.34  

Breakdown:
- OpenAI: $0.15  
- Claude Sonnet: $2.96  
- Gemini: $0.00 (free tier)  

This highlights the importance of efficient evaluation strategies in real-world AI systems.

---

## Technologies Used

- Promptfoo (prompt evaluation framework)  
- OpenAI API (`gpt-4o-mini`)  
- Anthropic Claude (Sonnet)  
- Google Gemini  
- Google Sheets (test dataset)  
- Node.js (Promptfoo runtime)  
- Python (environment setup and utilities)  

---

## Key Takeaways

- Prompt design significantly affects output quality  
- Emotional and role-based prompts can improve responses in some cases  
- Chain-of-Thought prompting helps with reasoning tasks  
- Automated evaluation pipelines are essential for scalable prompt engineering  
- Cost and token usage must be carefully managed when testing multiple models
_____________________________________________________________________________________________________________________________________________________
# AI Automation

#  Project Overview  AI Document Q&A Agent (n8n)

<p align="center">
  <img src="https://github.com/user-attachments/assets/04e3f96b-8a85-46f9-98f1-e26d8d4d453a" width="300" />
  <img src="https://github.com/user-attachments/assets/008033d4-9564-4320-be20-11cc44a90a8f" width="300" />
  <img src="https://github.com/user-attachments/assets/a3e96b88-0e91-4226-a72f-2e8f4056303c" width="300" />
</p>

This project is an AI-powered RAG (Retrieval-Augmented Generation) system built in n8n.
It allows you to upload a PDF document to Google Drive and ask questions about its content.
The workflow retrieves relevant text from the document using a vector database and generates accurate answers with OpenAI GPT-4o-mini.

📌How This Project Helps People and Organizations

This AI Document Q&A Agent can be extremely useful for anyone who works with large documents, manuals, reports, or internal files.
Instead of searching manually through long PDFs, users can simply ask questions and get accurate answers instantly.

📌Who Can Benefit

- Students & Researchers — quickly extract important information from academic papers

- Teams & Organizations — make internal documents searchable and interactive

- Customer Support — turn product manuals into smart, conversational knowledge bases

- Managers & Executives — access key insights from long reports without reading everything

- Educators — create instant Q&A systems for course materials

- Engineers / Developers — build custom chatbots for private documents

📌How It Helps

- Instant Information Retrieval
No need to scroll through a PDF — ask a question and get the exact answer.

- Automated Knowledge Extraction
Converts any document into a searchable knowledge base using AI.

- Context-Aware Answers
Uses the uploaded document as the only source, ensuring grounded and accurate responses.

- Saves Time
Reduces hours of manual reading, searching, and summarizing.

- Private & Secure
Your data stays inside your own n8n workflow and vector database.

- Increases Productivity
Teams can make faster decisions by retrieving essential information instantly.

📌Key Steps:

- Load a PDF file stored in Google Drive

- Split the document into text chunks

- Convert chunks into embeddings using OpenAI

- Store embeddings in a Pinecone vector database

- Retrieve the most relevant chunks based on user queries

- Generate context-aware answers using GPT-4o-mini

- Interact with the agent using n8n’s built-in chat interface

📌Output

- Accurate answers grounded in the uploaded PDF

- Fast, semantic search over document content

- Fully automated workflow for document processing

- Real-time Q&A capability through n8n


_____________________________________________________________________________________________________________________________________________________

# 🤖 AI Assistant for PhD Program Information (RAG-based Chatbot)
### [👉Click here to view the Live App](https://llms-phd-program.streamlit.app/)

<p align="center">
  <img src="https://github.com/user-attachments/assets/491fb663-11fd-480d-885c-56159a3879bd" width="900" />
</p>

## What I Have Done

I developed a Retrieval-Augmented Generation (RAG) chatbot application that allows users to interact with and query information from documents, specifically focused on PhD program details.

The system processes PDF documents, extracts and chunks the text, converts it into vector embeddings using OpenAI models, and stores them in a Pinecone vector database. When a user asks a question, the system retrieves the most relevant information from the database and generates a response using a language model.

This approach enables accurate, context-aware answers instead of generic responses.

### Business Value

This solution can be applied across multiple business domains:

- **Knowledge Management**: Enables organizations to query internal documents (policies, manuals, reports) efficiently.
- **Customer Support Automation**: Provides instant, context-aware answers based on company documentation.
- **Education & Training**: Helps users explore structured content such as academic programs or training materials.
- **Decision Support Systems**: Allows quick access to relevant insights from large datasets.

Overall, it reduces manual effort, improves information accessibility, and enhances user experience.
---

## Technologies Used

- **Python**
- **Streamlit** (UI and deployment)
- **OpenAI API** (embeddings and language model)
- **Pinecone** (vector database)
- **PyPDF** (PDF text extraction)
- **dotenv** (environment variable management)
  

---

# AI Meal Planner Agent
### [👉Click here to view the Live App](https://aimealplanneragent.streamlit.app/)

<p align="center">
  <img src="https://github.com/user-attachments/assets/23322977-2647-4e49-a86b-71271832a9a5" width="300" />
  <img src="https://github.com/user-attachments/assets/71fd7e60-feaa-4595-8975-7c2b6d824178" width="300" />
</p>

__________

## Summary

AI Meal Planner Agent is a Streamlit-based AI application that generates personalized meal plans from user-provided ingredients. The app uses OpenAI models to create healthy and structured meal recommendations based on calorie goals, meal preferences, and cooking styles.

Users can also:
- Download meal plans as PDF files
- Generate voice-guided cooking instructions
- Customize meals for breakfast, lunch, dinner, or full-day plans

---

## Why This Project Is Useful

This project helps users quickly create healthy meal plans without manually searching for recipes or calculating nutrition constraints.

It is useful for:
- People who want healthy meal suggestions
- Fitness-focused users tracking calories
- Users with limited ingredients at home
- Anyone interested in AI-powered productivity tools

The application combines AI-generated text, PDF generation, and AI voice synthesis into one interactive experience.

---

## Technologies Used

### Frontend / UI
- Streamlit

### AI Models
- OpenAI GPT-4.1-mini
- OpenAI Text-to-Speech (TTS)

### Backend / Logic
- Python

### PDF Generation
- ReportLab

### Other Python Libraries
- io.BytesIO

---

## Deployment

This project is deployed on Streamlit Cloud.

---

## Future Improvements

- Nutrition and macro tracking
- User authentication
- Saved meal history
- Multi-language support
- Grocery shopping list generation
- Database integration
- Image generation for meals

---
_____________________________________________________________________________________________________________________________________________________


# 𝕏 Tweet Generator with Reflection Agents
An AI-powered tweet generation application built with LangGraph, LangChain, OpenAI, and Streamlit.
### [👉Click here to view the Live App](https://tweet-generator-langgraph.streamlit.app/)

<img width="1079" height="613" alt="Screenshot 2026-05-13 004104" src="https://github.com/user-attachments/assets/a4df0007-95de-47fb-9e10-de9878d2b224" />


This project uses a reflection-based workflow where the AI:
1. Generates an initial tweet
2. Critiques and reflects on the output
3. Improves the tweet iteratively
4. Produces a final optimized version

## Features

- AI tweet generation
- Reflection and self-improvement loop
- Multi-step draft iterations
- Final optimized tweet output
- Streamlit interactive UI
- LangGraph state-based workflow
- OpenAI GPT integration

## Tech Stack

- Python
- Streamlit 
- LangChain
- LangGraph
- OpenAI API

---

## Deployment

This project is deployed on Streamlit Cloud.

---
