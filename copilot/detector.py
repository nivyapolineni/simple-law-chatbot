def detect_task(text: str) -> str:
    """
    Identifies the user's intent based on the input text.
    Returns one of: 'CONTRACT ANALYSIS', 'LEGAL Q&A', 'SUMMARIZATION', 'LEGAL DRAFTING', or 'UNKNOWN'.
    """
    text_lower = text.lower().strip()

    if not text_lower:
        return "UNKNOWN"

    # 1. Check for Drafting first as it's often a specific request
    if any(word in text_lower for word in ["draft", "write", "create a notice", "legal notice"]):
        return "LEGAL DRAFTING"

    # 2. Check for Contract keywords
    contract_keywords = ["agreement", "contract", "nda", "clause", "terms and conditions", "hereby", "party of the first part"]
    if any(keyword in text_lower for keyword in contract_keywords):
        return "CONTRACT ANALYSIS"

    # 3. Check for Question (LEGAL Q&A)
    # Questions usually end with ? or start with question words or contain keywords like 'explain'
    question_words = ("what", "how", "can", "is", "where", "why", "who", "which", "could", "should", "explain")
    if text_lower.endswith("?") or text_lower.startswith(question_words) or "what is" in text_lower or "how to" in text_lower:
        return "LEGAL Q&A"

    # 4. Check for Summarization
    # Typically long documents or explicit requests for summary
    if len(text.split()) > 50 or "summarize" in text_lower or "summary" in text_lower:
        return "SUMMARIZATION"

    return "UNKNOWN"

def is_simple_explanation_requested(text: str) -> bool:
    """
    Checks if the user specifically asked for a 'simple explanation'.
    """
    return "simple explanation" in text.lower()
