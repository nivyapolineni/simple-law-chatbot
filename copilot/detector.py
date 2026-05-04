def detect_task(text: str) -> str:
    """
    Identifies the user's intent based on the input text.
    Returns one of: 'CONTRACT ANALYSIS', 'LEGAL Q&A', 'SUMMARIZATION', 'LEGAL DRAFTING', or 'UNKNOWN'.
    """
    text_lower = text.lower().strip()

    if not text_lower:
        return "UNKNOWN"

    # 0. Check for Matter Management
    if any(phrase in text_lower for phrase in ["create matter", "open matter", "new matter", "view matter"]):
        return "MATTER MANAGEMENT"

    # 1. Check for Contract keywords first, especially if it's a long document
    contract_keywords = ["agreement", "contract", "nda", "clause", "terms and conditions", "hereby", "party of the first part"]
    if any(keyword in text_lower for keyword in contract_keywords) and len(text.split()) > 20:
        return "CONTRACT ANALYSIS"

    # 2. Check for Drafting (usually starting with a command)
    drafting_commands = ["draft", "write", "create a notice", "legal notice"]
    if any(word in text_lower[:50] for word in drafting_commands):
        return "LEGAL DRAFTING"

    # 3. Fallback for shorter contract mentions
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
