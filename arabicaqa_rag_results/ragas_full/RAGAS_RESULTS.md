# RAGAS Full Evaluation Results

Judge: gemma2:2b (Ollama)
Models: LLAMA, MISTRAL

  model       subset  n_questions  answer_relevancy  faithfulness  context_recall  context_precision  answer_correctness  answer_similarity
  LLAMA   ANSWERABLE            5            0.8602        0.8333          0.6000                NaN              0.9454             0.8269
  LLAMA UNANSWERABLE            5            0.6873        1.0000          0.9167                NaN                 NaN             0.7575
MISTRAL   ANSWERABLE            5            0.0000        1.0000          0.6000                NaN                 NaN             0.8134
MISTRAL UNANSWERABLE            5               NaN        0.5000          1.0000                NaN                 NaN             0.7307