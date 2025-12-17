# Arabic RAG Leaderboard Result


## Overall (unanswerables mapped to "غير موجود في السياق")

| Model               | EM      | EM25     |
|---------------------|---------|----------|
| Llama-3.1-8B        | 10.70% | 10.70% |
| Mistral-7B-Instruct | 13.50% | 13.50% |
| **Winner**          | —       | **Mistral-7B-Instruct** (+2.80 pts) |

## Breakdown

Answerable rows: **500**  
Unanswerable rows: **500** (gold empty mapped to **غير موجود في السياق**)

| Model               | Ans EM   | Ans EM25 | No-Ans Acc |
|---------------------|----------|----------|------------|
| Llama-3.1-8B        | 4.20% | 4.20% | 27.20% |
| Mistral-7B-Instruct | 1.20% | 1.20% | 31.60% |
