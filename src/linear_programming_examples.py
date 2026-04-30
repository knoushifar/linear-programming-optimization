"""Linear programming examples solved with SciPy.

The problems are formulated as maximization LPs:

    maximize     c^T x
    subject to   A x <= b
                 x >= 0

SciPy's linprog solves minimization problems, so each objective is multiplied by -1.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linprog


@dataclass(frozen=True)
class LinearProgrammingProblem:
    """Container for a linear programming maximization problem."""

    name: str
    objective: list[float]
    constraints: list[list[float]]
    bounds: list[float]


def solve_maximization_problem(problem: LinearProgrammingProblem) -> dict[str, object]:
    """Solve one maximization LP and return a dictionary of results."""
    objective = np.array(problem.objective, dtype=float)
    constraints = np.array(problem.constraints, dtype=float)
    bounds = np.array(problem.bounds, dtype=float)

    result = linprog(
        c=-objective,
        A_ub=constraints,
        b_ub=bounds,
        bounds=[(0, None)] * len(objective),
        method="highs",
    )

    if not result.success:
        return {
            "problem": problem.name,
            "status": "No optimal solution found",
            "objective_value": None,
            "solution": None,
        }

    return {
        "problem": problem.name,
        "status": "Optimal",
        "objective_value": round(float(-result.fun), 6),
        "solution": [round(float(value), 6) for value in result.x],
    }


def get_problems() -> list[LinearProgrammingProblem]:
    """Return the LP examples from the original notebook."""
    return [
        LinearProgrammingProblem(
            name="1.3",
            objective=[1, 2],
            constraints=[
                [1, -4],
                [-2, 1],
                [-3, 4],
                [2, 1],
            ],
            bounds=[4, 2, 12, 8],
        ),
        LinearProgrammingProblem(
            name="3.3",
            objective=[1, 3],
            constraints=[
                [1, -2],
                [-2, 1],
                [5, 3],
            ],
            bounds=[0, 4, 15],
        ),
        LinearProgrammingProblem(
            name="5.2",
            objective=[3, 2, 1],
            constraints=[
                [3, -3, 2],
                [-1, 2, 1],
            ],
            bounds=[3, 6],
        ),
        LinearProgrammingProblem(
            name="21.3",
            objective=[0.8, 1.11, 1.3],
            constraints=[
                [172.8, 96, 38.4],
                [19.2, 57.6, 96],
                [0, 38.4, 57.6],
            ],
            bounds=[150, 100, 50],
        ),
        LinearProgrammingProblem(
            name="27.3",
            objective=[2, 1, 6, -4],
            constraints=[
                [1, 2, 4, -1],
                [2, 3, -1, 1],
                [1, 0, 1, 1],
            ],
            bounds=[6, 12, 2],
        ),
    ]


def main() -> None:
    """Solve all LP examples and save the results."""
    results = [solve_maximization_problem(problem) for problem in get_problems()]
    results_df = pd.DataFrame(results)

    output_path = Path(__file__).resolve().parents[1] / "results" / "solutions.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results_df.to_csv(output_path, index=False)

    print(results_df.to_string(index=False))
    print(f"\nSolutions saved to: {output_path}")


if __name__ == "__main__":
    main()
