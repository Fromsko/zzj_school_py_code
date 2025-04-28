# Project Structure Plan

Here's a summary of the changes made to conform to Rye's conventions for a Python library with a sub-package:

1.  **Renamed the top-level package:** Renamed `my_library` back to `school_code`. (You need to rename the directory `src/my_library` back to `src/school_code` manually)
2.  **Ensured each experiment is a sub-package:** Each experiment (e.g., `exp_1`) is a sub-package within `school_code`.
3.  **Updated the `pyproject.toml` file:**
    *   The `name` field was updated to `school-code`.
    *   The `packages` section was updated to include the sub-package `exp_1`.
    *   The `[project.scripts]` section was updated to reflect the new top-level package name.
    *   The `[tool.rye.scripts]` section was updated to reflect the new top-level package name.

Here's the recommended directory structure:

```
project_root/
├── pyproject.toml
├── src/
│   └── school_code/       # Top-level package
│       ├── __init__.py   # Code for the top-level package (can be empty)
│       └── exp_1/        # Sub-package
│           └── __init__.py  # Code for the sub-package
└── ... (other files like README.md, tests/, etc.)