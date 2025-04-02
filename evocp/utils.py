import signal
import json

# === Timeout Handling ===

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

# Register signal handler for timeouts
signal.signal(signal.SIGALRM, timeout_handler)

# === Dataset Loader ===

def load_math_problems(jsonl_path):
    """Loads a JSONL dataset where each line is a problem dict."""
    problems = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            problems.append(json.loads(line.strip()))
    return problems