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

The application is structured as follows:

### UI Components

- `src/ui/chat.py`: Chat interface logic
- `src/ui/profile.py`: Profile/sidebar and expander UI
- `src/ui/utils.py`: UI utility functions (e.g., clear chat)

### Backend Components

- `src/logic/backend_interface.py`: Interface for backend/AI agent connection
- `src/logic/data_loader.py`: Loads and formats resume data
- `src/agents/resume_agent.py`: LangChain-based agent for answering resume questions

The main entrypoint is `src/main.py`.

```bash
# Run using streamlit
streamlit run src/main.py

# Alternative way to run streamlit
python -m streamlit run src/main.py
```

## Features

- Interactive chat interface for querying resume information
- Static profile information display
- Toggle between mock responses and actual LLM-powered responses
- Backend powered by LangChain and GPT-4o-mini

## Upcoming Features

- Question suggestions
- Resume download
- Enhanced profile display
- Full resume data integration
- LinkedIn/GitHub connectivity

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/ui/test_chat.py
```
