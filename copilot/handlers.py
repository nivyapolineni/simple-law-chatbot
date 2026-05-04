import json
import os
from typing import Dict, Any

MATTERS_FILE = "matters.json"

def _load_matters():
    if os.path.exists(MATTERS_FILE):
        with open(MATTERS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def _save_matters(matters):
    with open(MATTERS_FILE, 'w') as f:
        json.dump(matters, f, indent=4)

def handle_matter_management(text: str) -> Dict[str, Any]:
    """
    Handles creation and retrieval of legal matters.
    """
    text_lower = text.lower()
    matters = _load_matters()

    if "create matter" in text_lower or "new matter" in text_lower:
        # Simple parser for "create matter [name] with details [details]"
        name = "Untitled Matter"
        details = "No details provided."

        if "matter" in text_lower:
            parts = text.split("matter", 1)[1].strip().split("with details", 1)
            name = parts[0].strip() or name
            if len(parts) > 1:
                details = parts[1].strip()

        matters[name] = {
            "name": name,
            "details": details,
            "status": "Open"
        }
        _save_matters(matters)
        return {"action": "CREATE", "matter": matters[name]}

    elif "open matter" in text_lower or "view matter" in text_lower:
        name = text.split("matter", 1)[1].strip() if "matter" in text_lower else ""
        if name in matters:
            return {"action": "OPEN", "matter": matters[name]}
        else:
            return {"action": "ERROR", "message": f"Matter '{name}' not found."}

    return {"action": "ERROR", "message": "Could not understand matter command."}

def handle_contract_analysis(text: str) -> Dict[str, Any]:
    """
    Performs CONTRACT ANALYSIS.
    """
    # In a real app, this would use an LLM. Here we provide a structured mock or simple extraction.
    return {
        "Summary": "This document appears to be a formal agreement between two parties regarding their mutual obligations and rights.",
        "Key Clauses": [
            "Confidentiality: Protecting sensitive information.",
            "Termination: How the agreement can be ended.",
            "Liability: Limits on legal responsibility.",
            "Payment Terms: Details on financial obligations."
        ],
        "Obligations": {
            "Party A": "Must deliver services as described.",
            "Party B": "Must provide payment within the stipulated time."
        },
        "Risks": [
            "Termination clause might be too one-sided.",
            "Liability limits may not be sufficient for high-risk activities."
        ],
        "Suggestions": [
            "Ensure the governing law is specified (e.g., laws of India).",
            "Clarify the dispute resolution mechanism (e.g., Arbitration in New Delhi)."
        ]
    }

def handle_legal_qa(text: str) -> Dict[str, Any]:
    """
    Performs LEGAL Q&A.
    """
    # Simple keyword-based mock for demonstration
    if "cheating" in text.lower():
        return {
            "Explanation": "Cheating is defined as dishonestly inducing a person to deliver property or to consent to the retention of property.",
            "Sections": "Section 420 of the Indian Penal Code (IPC).",
            "Example": "If someone sells a fake gold ring claiming it is real, they can be charged under IPC Section 420."
        }
    elif "theft" in text.lower():
        return {
            "Explanation": "Theft involves moving movable property out of the possession of any person without that person's consent with dishonest intention.",
            "Sections": "Section 378 (Definition) and Section 379 (Punishment) of the IPC.",
            "Example": "Taking a neighbor's bicycle without asking, with the intention to keep it, constitutes theft."
        }
    else:
        return {
            "Explanation": "I am not certain about the specific legal details for this question.",
            "Sections": "N/A",
            "Example": "Please provide more details or consult a legal professional."
        }

def handle_summarization(text: str) -> Dict[str, Any]:
    """
    Performs SUMMARIZATION.
    """
    return {
        "Short Summary": "The provided document discusses legal frameworks or agreements relevant to the context of Indian law.",
        "Key Points": [
            "Identifies the main parties involved.",
            "Outlines the primary objectives.",
            "Lists specific rights and duties."
        ],
        "Implications": "Failure to comply with these terms may result in legal action or financial penalties."
    }

def handle_legal_drafting(text: str) -> Dict[str, Any]:
    """
    Performs LEGAL DRAFTING.
    """
    return {
        "Sender": "[Your Name/Organization Name]",
        "Recipient": "[Recipient Name/Organization Name]",
        "Subject": "LEGAL NOTICE REGARDING [Insert Subject Matter]",
        "Body": "I am writing this notice to formally demand [Insert Demand]. This is based on [Insert Legal Basis]. Failure to comply within [X] days will result in further legal action.",
        "Closing": "Yours faithfully,\n[Your Signature]"
    }

def handle_simple_explanation(text: str) -> str:
    """
    Explains like to a 15-year-old.
    """
    return "Think of this law like a rule in a school game. If you break the rule to gain an unfair advantage, you get a 'penalty' (like a timeout or detention). In the real world, these 'penalties' are much more serious and are decided by a judge."
