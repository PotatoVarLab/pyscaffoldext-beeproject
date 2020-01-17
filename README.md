# pyscaffoldext-beeproject

[PyScaffold] extension tailored for my own simple structured projects. This extension is powered by *pyscaffoldext-dsproject*

The final directory structure looks like:
```
Project_Dir
├── AUTHORS.rst             <- List of developers and maintainers.
├── CHANGELOG.rst           <- Changelog to keep track of new features and fixes.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── data
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── src
│   └── Project_Name        <- Actual Python project which can be deploy to production
│       └── environment.yaml                <- Actual Python project need conda environment yaml file
│       └── run_python_project_main.py      <- Actual Python project some one part main execute script
│       └── supervisor_project_main.ini     <- Actual Python project some one part main script supervisor ini template file
│       └── project_name                    <- Actual Python project some one package template
│       └── __init__.py                     <- Use for sphinx auto documents
├── tests                   <- Unit tests which can be run with `py.test`.
```

## Usage

Just install this package with `pip install pyscaffoldext-beeproject`
and note that `putup -h` shows a new option `--beeproject`.
Creating a data science project is then as easy as:
```
putup --beeproject Simple_Project
```

## Note

This project has been set up using PyScaffold 3.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.

[PyScaffold]: https://pyscaffold.org/
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Jupyter]: https://jupyter.org/
[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
