import nox


nox.options.sessions = "lint", "tests"


# ---- Configuration ----


SUPPORTED_PYTHON_VERSIONS = ["3.6", "3.7", "3.8"]

PYTEST_OPTIONS = ["--cov=austin", "--cov-report", "term-missing"]

LINT_LOCATIONS = ["austin", "test", "noxfile.py"]

MYPY_LOCATIONS = LINT_LOCATIONS[:1]


# ---- Sessions ----


@nox.session(python=SUPPORTED_PYTHON_VERSIONS)
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "python", "-m", "pytest", *PYTEST_OPTIONS)


@nox.session(python=SUPPORTED_PYTHON_VERSIONS)
def lint(session):
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *LINT_LOCATIONS)


@nox.session(python=SUPPORTED_PYTHON_VERSIONS)
def mypy(session):
    session.install("mypy")
    session.run("mypy", *MYPY_LOCATIONS)
