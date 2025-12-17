# RAGAS Full Evaluation Results

Judge: gemma2:2b (Ollama)
Models: LLAMA, MISTRAL

| model   | subset       |   n_questions |   answer_relevancy |   faithfulness |   context_recall |   context_precision |   answer_correctness |   answer_similarity |
|:--------|:-------------|--------------:|-------------------:|---------------:|-----------------:|--------------------:|---------------------:|--------------------:|
| LLAMA   | ANSWERABLE   |           500 |             0.5866 |         0.8111 |           0.6087 |              0.2386 |               0.582  |              0.8396 |
| LLAMA   | UNANSWERABLE |           500 |             0.6758 |         0.7993 |           0.8991 |              0.048  |               0.5057 |              0.7497 |
| MISTRAL | ANSWERABLE   |           500 |             0.5027 |         0.8614 |           0.6096 |              0.2309 |               0.5218 |              0.8231 |
| MISTRAL | UNANSWERABLE |           500 |             0.6078 |         0.8381 |           0.9054 |              0.0476 |               0.4899 |              0.7401 |