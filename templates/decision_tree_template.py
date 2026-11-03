# Auto-generated deterministic classifier
# Continuously synthesized and evolved by llm-distiller
# Latency: < 0.08ms | API Cost: $0.00
import re
from typing import Optional

def classify_intent_deterministic(text: str) -> Optional[str]:
    t = text.lower()

    # Rule Cluster: AUTH
    if re.search(r'\b(account|cannot|credentials|failed|login|password|reset|with)\b', t):
        return 'AUTH'

    # Rule Cluster: BILLING
    if re.search(r'\b(back|card|credit|how|money|please|refund|subscription)\b', t):
        return 'BILLING'

    # Rule Cluster: BUG
    if re.search(r'\b(api|application|crashed|error|internal|server|the|throws)\b', t):
        return 'BUG'

    # Fallback to cloud LLM if no deterministic invariant matched
    return None
