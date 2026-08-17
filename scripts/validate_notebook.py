"""Validate the customer churn notebook without requiring the private dataset."""

from __future__ import annotations

import ast
from pathlib import Path

import nbformat
from nbformat.validator import validate


NOTEBOOK = Path("customer_churn_logistic_regression.ipynb")


def python_source(source: str) -> str:
    """Remove notebook-only commands while preserving normal Python."""
    lines = []
    skip_cell_magic = False

    for index, line in enumerate(source.splitlines()):
        stripped = line.lstrip()

        if index == 0 and stripped.startswith("%%"):
            skip_cell_magic = True
            break

        if stripped.startswith(("%", "!")):
            continue

        lines.append(line)

    return "" if skip_cell_magic else "\n".join(lines)


def main() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    validate(notebook)

    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    if not code_cells:
        raise ValueError("Notebook contains no Python code cells.")

    compiled = 0
    for cell_number, cell in enumerate(code_cells, start=1):
        source = python_source(cell.source)
        if not source.strip():
            continue

        try:
            ast.parse(source, filename=f"{NOTEBOOK}:code-cell-{cell_number}")
        except SyntaxError as exc:
            raise SyntaxError(
                f"Python syntax validation failed in code cell {cell_number}: {exc}"
            ) from exc
        compiled += 1

    if compiled == 0:
        raise ValueError("Notebook contains no compilable Python cells.")

    print(
        f"Validated {NOTEBOOK}: schema is valid and "
        f"{compiled} Python code cells compile successfully."
    )


if __name__ == "__main__":
    main()
