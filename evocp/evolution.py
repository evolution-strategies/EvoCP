# evolution.py

import requests
import json
import random
import re
import signal

# Timeout Setup
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

signal.signal(signal.SIGALRM, timeout_handler)

# ANSI Colors for Console
COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
RESET_COLOR = "\033[0m"

from evocp.api import solver_llm, evaluator_llm, correctness_llm
from evocp.cognitive_ops import COGNITIVE_OPERATIONS, BASE_PROMPT


def mutate_cognitive_operations(prompt, mutation_probability=0.3):
    lines = prompt.splitlines()
    new_lines = []
    for line in lines:
        if re.match(r'^\d+\.', line):
            if random.random() < mutation_probability:
                number = line.split('.')[0]
                new_lines.append(f"{number}. {random.choice(COGNITIVE_OPERATIONS)}")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def run_evolution(problem_text, reference_answer, max_generations=50, generation_timeout=200):
    parent_prompt = BASE_PROMPT
    parent_solution = solver_llm(parent_prompt, problem_text)
    parent_fitness = evaluator_llm(parent_solution)
    generations_used = 0
    solved = False

    for gen in range(max_generations):
        print(f"{COLORS[3]}=== Generation {gen+1} ==={RESET_COLOR}")
        try:
            signal.alarm(generation_timeout)
            child_prompt = mutate_cognitive_operations(parent_prompt, mutation_probability=0.3)
            child_solution = solver_llm(child_prompt, problem_text)
            child_fitness = evaluator_llm(child_solution)
            print(f"Parent fitness: {parent_fitness}, Child fitness: {child_fitness}")

            if child_fitness >= parent_fitness:
                parent_prompt, parent_solution, parent_fitness = child_prompt, child_solution, child_fitness
                print(f"Child replaces parent with fitness: {child_fitness}")

            if correctness_llm(parent_solution, reference_answer):
                print(f"{COLORS[1]}Correct answer found in generation {gen+1}!{RESET_COLOR}")
                generations_used = gen + 1
                solved = True
                break
        except TimeoutException:
            print(f"{COLORS[0]}Generation {gen+1} timed out.{RESET_COLOR}")
            break
        finally:
            signal.alarm(0)

    return parent_prompt, parent_solution, generations_used, solved