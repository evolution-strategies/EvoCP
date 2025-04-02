import requests
import json
import re

OLLAMA_API_URL = "http://0.0.0.0:11434/api/chat"
MODEL_NAME_SOLVER = "llama3.2"
MODEL_NAME_EVALUATOR = "llama3.2"
MODEL_NAME_CORRECTNESS = "llama3.2"

def ollama_api_call(messages, model, stream=False):
    messages.insert(0, {
        "role": "system",
        "content": "You do NOT remember any previous interactions. Treat each request independently."
    })
    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": model, "messages": messages, "stream": stream
        })
        response.raise_for_status()
        if not stream:
            collected = []
            for line in response.text.strip().split("\n"):
                if line.strip():
                    data = json.loads(line.strip())
                    if "message" in data and "content" in data["message"]:
                        collected.append(data["message"]["content"])
            return "".join(collected)
        return ""
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Request Error: {e}")

def solver_llm(prompt, problem_text):
    messages = [
        {"role": "system", "content": "You are a structured problem solver following cognitive reasoning steps."},
        {"role": "user", "content": prompt + problem_text}
    ]
    return ollama_api_call(messages, model=MODEL_NAME_SOLVER).strip()

def evaluator_llm(solution):
    eval_prompt = f"""You are a strict evaluator.
Forget all previous interactions.
Return a single floating-point score from 0.0 to 1.0.

Solution:
{solution}

Criteria:
1. Mathematical Accuracy.
2. Clarity.
3. Depth.
4. Conciseness.
5. No Leakage.

Return only a floating-point score in [0,1].
"""
    messages = [{"role": "user", "content": eval_prompt}]
    response = ollama_api_call(messages, model=MODEL_NAME_EVALUATOR)
    match = re.search(r"(\d+(\.\d+)?)", response)
    return max(0.0, min(1.0, float(match.group(1)))) if match else 0.0

def correctness_llm(solution, reference_answer):
    messages = [
        {"role": "system", "content": "You are a correctness checker for mathematical solutions."},
        {"role": "user", "content": f"SOLVER'S OUTPUT:\n{solution}\n\nREFERENCE ANSWER:\n{reference_answer}\n\nDoes the solver's numeric result match? Reply 'yes' or 'no'."}
    ]
    response = ollama_api_call(messages, model=MODEL_NAME_CORRECTNESS).strip().lower()
    return "yes" in response and "no" not in response