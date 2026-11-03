---
name: llm-distiller
description: >-
  [WHAT IT DOES]: Compiles repetitive LLM inference tasks (intent routing, text classification, unstructured data extraction)
  into zero-cost, sub-millisecond, deterministic Python/TypeScript code or compact offline micro-models.
  [WHEN TO USE]: Use when replacing expensive cloud LLM API calls with deterministic code, reducing latency from seconds
  to microseconds, eliminating API billing costs, or removing probabilistic hallucinations from predictable workflows.
  [WHEN NOT TO USE]: Do NOT use for open-ended creative story writing, subjective prose generation, or novel reasoning tasks.
---

# LLM Distiller: Cognitive-to-Deterministic Compiler

```
  +---------------------------------------------------------------------------------+
  |                                 LLM DISTILLER                                   |
  |             Cognitive-to-Deterministic Compilation Pipeline                     |
  +---------------------------------------------------------------------------------+

  [Production LLM Inference Logs]
  - 1,000+ Raw Input / Output Pairs
  - High Latency (1,500ms) & Token API Invoices
                        |
                        v
          [Mutual Information & Token Scoring]
          - TF-IDF Discriminator Extraction
          - Precision / Recall / F1 Optimization
          - Decision Boundary Identification
                        |
                        v
        +---------------+---------------+
        |                               |
        v                               v
  [Pure Regex / AST Rules]     [Deterministic Decision Tree]
        |                               |
        +---------------+---------------+
                        |
                        v
      [Behavioral Parity & Accuracy Benchmark]
      - Evaluates Against Ground Truth Dataset
      - Target Threshold: >= 99.5% Accuracy
                        |
        +---------------+---------------+
        |                               |
  [Meets Parity Threshold]     [Fails Threshold (< 99.5%)]
        v                               v
  [Synthesize Zero-Token Code] [Isolate Ambiguous Edge Cases]
  - 0.1ms Local Function       - Retain Narrow LLM Fallback Branch
  - $0.00 / Month Cost
```

---

## 1. When to Activate

Trigger `llm-distiller` when:
- **High-Volume LLM Classification:** Routing support tickets, spam filtering, sentiment tagging, intent classification.
- **Structured Data Extraction:** Pulling IDs, invoice amounts, dates, or emails from unstructured text using prompts.
- **Latency Bottlenecks:** Real-time applications requiring responses under 10ms where LLM streaming is too slow.
- **Cost Reduction:** Cutting cloud AI bills (OpenAI, Anthropic, Gemini API) on repetitive tasks.

---

## 2. Distillation Runbook

### Step 1: Ingest High-Confidence Trace Logs
Collect JSONL traces from past executions:
```json
{"input": "Please cancel my subscription and issue a refund", "output": "BILLING_REFUND"}
```

### Step 2: Fit and Score Decision Invariants
Run the distillation engine to compute mutual information scores across all tokens:
```bash
python scripts/distill_traces.py --demo
```
- Scans tokens and n-grams for dominant predictive power.
- Filters out noise words while preserving high-precision anchors.

### Step 3: Synthesize Deterministic Code
The distiller outputs a drop-in replacement Python or TypeScript function:
```python
def classify_deterministic(text: str) -> Optional[str]:
    # High-speed deterministic regex branches
    if re.search(r"\b(refund|chargeback|cancel)\b", text.lower()):
        return "BILLING_REFUND"
    return None  # Fallback to LLM only if ambiguous
```

### Step 4: Validate ROI & Parity
- Run the synthesized code against the evaluation split.
- Ensure accuracy $\ge 99.5\%$.
- Calculate the annualized cost reduction and user latency improvement.

---

## 3. Reference Files
- [distill_traces.py](./scripts/distill_traces.py): Token mutual information analyzer and code generator.
- [decision_tree_template.py](./templates/decision_tree_template.py): Synthesized deterministic classifier template.
