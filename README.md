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
