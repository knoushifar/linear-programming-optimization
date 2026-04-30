# Linear Programming Optimization Examples

This project contains a set of linear programming (LP) examples solved using Python. The original work was written in a Jupyter Notebook with `docplex`, and the repository version reorganizes it into a cleaner GitHub-ready structure with a reusable Python script, requirements file, and documented results.

## Project Overview

Linear programming is an optimization technique used to maximize or minimize a linear objective function subject to linear constraints. This project demonstrates how several LP problems can be formulated and solved computationally.

The examples include:

- Two-variable maximization problems
- Three-variable maximization problems
- Resource-allocation style constraints
- Multi-variable LP formulations
- Automated solution reporting

## Repository Structure

```text
linear-programming-optimization/
│
├── notebooks/
│   └── lp_original.ipynb
│
├── src/
│   └── linear_programming_examples.py
│
├── results/
│   └── solutions.csv
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Methods Used

The project solves LP problems in the following standard form:

```text
maximize     cᵀx
subject to   Ax ≤ b
             x ≥ 0
```

The GitHub-ready implementation uses `scipy.optimize.linprog`. Since SciPy solves minimization problems by default, each maximization problem is converted into a minimization problem by minimizing the negative objective function.

## Example Problems

The script includes five LP examples adapted from the original notebook:

| Problem | Variables | Objective Type |
|---|---:|---|
| 1.3 | 2 | Maximization |
| 3.3 | 2 | Maximization |
| 5.2 | 3 | Maximization |
| 21.3 | 3 | Maximization |
| 27.3 | 4 | Maximization |

## Results

The computed optimal solutions are saved in:

```text
results/solutions.csv
```

Summary of results:

| Problem | Optimal Objective Value |
|---|---:|
| 1.3 | 10.5455 |
| 3.3 | 13.9091 |
| 5.2 | 38.0000 |
| 21.3 | 1.6686 |
| 27.3 | 9.3333 |

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/linear-programming-optimization.git
cd linear-programming-optimization
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/linear_programming_examples.py
```

## Original Notebook

The original notebook is kept in:

```text
notebooks/lp_original.ipynb
```

The notebook uses `docplex`, while the cleaned script uses SciPy for easier installation and reproducibility.

## Skills Demonstrated

- Mathematical optimization
- Linear programming formulation
- Python scripting
- Scientific computing with SciPy
- Reproducible project organization
- GitHub-ready documentation

## Notes

This is a compact academic/portfolio project. It is best used as a supporting project alongside larger machine learning or data science projects.

## License

This project is licensed under the MIT License.
