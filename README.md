# careerchat

## Installation

```bash
# Install Python 3.12
uv python install 3.12

# Pin specific Python version
uv python pin 3.12.10

# Create virtual environment
uv venv --python 3.12.10
source .venv/Scripts/activate
```

## Package Management with UV

### UV Sync

`uv sync` is a command that synchronizes your project's dependencies with the requirements specified in your project files (like `pyproject.toml` or `requirements.txt`). It ensures that your virtual environment matches exactly what's defined in your project configuration.

Usage:

```bash
# Sync all dependencies
uv sync

# Sync with specific requirements file
uv sync requirements.txt
```

### UV Lock

`uv lock` manages dependency locking for your project. It creates and updates a lockfile that ensures reproducible builds by pinning exact versions of all dependencies.

Usage:

```bash
# Generate or update lockfile
uv lock

# Upgrade specific package in lockfile
uv lock --upgrade package polars

# Generate lockfile from requirements
uv lock requirements.txt
```

The lockfile (usually `uv.lock`) contains the exact versions of all dependencies and their sub-dependencies, ensuring consistent installations across different environments.

## Development Setup

```bash
# Install development dependencies
uv pip install -e ".[dev]"
```

## Code Quality

```bash
# Run code checks using ruff
uvx ruff check
```

## Running the Application

```bash
# Run using streamlit
streamlit run your_script.py [-- script args]

# Alternative way to run streamlit
python -m streamlit run your_script.py
```
