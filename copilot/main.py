import sys
from copilot.detector import detect_task, is_simple_explanation_requested
from copilot.handlers import (
    handle_contract_analysis,
    handle_legal_qa,
    handle_summarization,
    handle_legal_drafting,
    handle_simple_explanation,
    handle_matter_management
)
from copilot.formatter import format_output

def run_copilot(user_input: str):
    if not user_input.strip():
        print("Please provide some input.")
        return

    task_type = detect_task(user_input)
    simple_req = is_simple_explanation_requested(user_input)

    data = None
    simple_explanation = None

    if task_type == "MATTER MANAGEMENT":
        data = handle_matter_management(user_input)
    elif task_type == "CONTRACT ANALYSIS":
        data = handle_contract_analysis(user_input)
    elif task_type == "LEGAL Q&A":
        data = handle_legal_qa(user_input)
    elif task_type == "SUMMARIZATION":
        data = handle_summarization(user_input)
    elif task_type == "LEGAL DRAFTING":
        data = handle_legal_drafting(user_input)

    if simple_req:
        simple_explanation = handle_simple_explanation(user_input)

    output = format_output(task_type, data, simple_explanation)
    print(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        run_copilot(user_input)
    else:
        print("AI Legal Copilot - specialized in Indian law")
        print("Type 'exit' to quit.")
        while True:
            try:
                user_input = input("\nHow can I help you? > ")
                if user_input.lower() in ["exit", "quit"]:
                    break
                run_copilot(user_input)
            except (KeyboardInterrupt, EOFError):
                break
