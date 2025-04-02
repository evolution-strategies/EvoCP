# EvoCP: Evolutionary Cognitive Prompting

This project implements an evolutionary prompt optimization framework using cognitive operations and local language models.

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


