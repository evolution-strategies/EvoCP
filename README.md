# EvoCP: Evolutionary Cognitive Prompting

This project implements an evolutionary prompt optimization framework using cognitive operations and local language models.
Associated with the paper “Evolutionary Cognitive Prompting for Enhancing the Capabilities of Language Models”, presented at the IEEE Conference on Artificial Intelligence 2025, Santa Clara.

## Abstract
This paper presents an evolutionary algorithm (EA) based agent approach for optimizing prompt-based mathematical problem-solving in language models (LMs). The system follows an agent-based evolutionary approach, where a single cognitive prompt undergoes iterative mutation and selection based on solution quality. A problem-solving agent generates solutions, a fitness evaluation agent scores responses without ground truth access, and a correctness verification agent terminates evolution upon identifying a correct solution. Evaluated on the MATH500 benchmark with the Llama 3.2 3B model, our approach demonstrates that evolutionary cognitive prompting (EvoCP) improves accuracy and accelerates convergence, highlighting the potential of EAs for improving LM reasoning in mathematical domains. The solve rate increases from 0.15 to 0.85, showing that EvoCP enables a compact LM to achieve significantly higher problem-solving capabilities.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start Ollama API server locally
3. Run the experiment: `python main.py`

## Project Structure

The EvoCP codebase is structured for clarity, modularity, and reproducibility:

| File / Module              | Purpose                                                        |
|----------------------------|----------------------------------------------------------------|
| `main.py`                  | Entry point for running EvoCP on MATH500                       |
| `evocp/evolution.py`       | Core evolutionary algorithm and mutation logic                 |
| `evocp/api.py`             | Interfaces with local LLMs for solving, scoring, and verifying |
| `evocp/cognitive_ops.py`   | Contains cognitive operations and base prompt                  |
| `evocp/utils.py`           | Dataset loading and timeout logic                              |
| `tests/test_mutation.py`   | Unit test for mutation operator                                |
| `data/math500.jsonl`       | Input dataset with 500 math problems                           |
| `results/`                 | Directory for generated output                                 |

## License
MIT

The `math500.jsonl` benchmark is derived from:
Dan Hendrycks et al., "Measuring Mathematical Problem Solving With the MATH Dataset" (2021)  
https://github.com/hendrycks/math  
Licensed under the MIT License.


