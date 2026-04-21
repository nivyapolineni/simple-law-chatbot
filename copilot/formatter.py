from typing import Dict, Any

DISCLAIMER = "\nDisclaimer:\nThis is not legal advice. Please consult a qualified lawyer."

def format_output(task_type: str, data: Any, simple_explanation: str = None) -> str:
    """
    Formats the output according to the specified structure.
    """
    if task_type == "UNKNOWN":
        return f"[UNKNOWN]\n\nI am not certain about your request. Please clarify if you want contract analysis, legal Q&A, summarization, or legal drafting.{DISCLAIMER}"

    output = f"[{task_type}]\n\n"

    if task_type == "CONTRACT ANALYSIS":
        output += f"Summary:\n{data['Summary']}\n\n"
        output += "Key Clauses:\n" + "\n".join([f"- {c}" for c in data['Key Clauses']]) + "\n\n"
        output += "Obligations:\n"
        for party, obligation in data['Obligations'].items():
            output += f"- {party}: {obligation}\n"
        output += "\nRisks:\n" + "\n".join([f"- {r}" for r in data['Risks']]) + "\n\n"
        output += "Suggestions:\n" + "\n".join([f"- {s}" for s in data['Suggestions']])

    elif task_type == "LEGAL Q&A":
        output += f"Summary:\n{data['Explanation']}\n\n"
        output += f"Key Points:\n- Relevant Section(s): {data['Sections']}\n\n"
        output += f"Example:\n{data['Example']}"

    elif task_type == "SUMMARIZATION":
        output += f"Summary:\n{data['Short Summary']}\n\n"
        output += "Key Points:\n" + "\n".join([f"- {p}" for p in data['Key Points']]) + "\n\n"
        output += f"Implications:\n{data['Implications']}"

    elif task_type == "LEGAL DRAFTING":
        output += "Summary:\nDrafting a formal legal notice based on the provided request.\n\n"
        output += "Key Points:\n- Formal professional tone\n- Clear sender and recipient identification\n- Explicit legal basis and demand\n\n"
        output += "Legal Notice Draft:\n"
        output += f"From: {data['Sender']}\n"
        output += f"To: {data['Recipient']}\n"
        output += f"Subject: {data['Subject']}\n\n"
        output += f"Body:\n{data['Body']}\n\n"
        output += f"{data['Closing']}"

    if simple_explanation:
        output += f"\n\n--- SIMPLE EXPLANATION ---\n{simple_explanation}"

    output += DISCLAIMER
    return output
