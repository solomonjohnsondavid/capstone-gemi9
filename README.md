## Gemi9 – Agentic Code Review & Testing Orchestrator

Gemi9 is a small agentic system built with **Google's Agent Development Kit (ADK)**.  
It exposes a single **orchestrator agent** that routes work to specialized sub‑agents for:

- **Pull Request review & GitHub automation**
- **Unit testing assistance**

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd gemi9
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # on macOS / Linux
# .venv\Scripts\activate   # on Windows (PowerShell / cmd)
```

### 3. Install dependencies

If you use **uv**:

```bash
uv sync
```

Or with plain **pip**:

```bash
pip install -e .  # or: pip install .
```

The core runtime dependency declared in `pyproject.toml` is:

- `google-adk==1.16.0`

---

## Configuration

Create an `.env` file at the project root (same directory as `pyproject.toml`) with at least:

```env
ORCHESTRATOR_AGENT_NAME=gemi9-orchestrator
PULL_REQUEST_AGENT_NAME=gemi9-pr-agent
UNIT_TESTING_AGENT_NAME=gemi9-test-agent

ORCHESTRATOR_AGENT_MODEL=<your-orchestrator-model-id>
PULL_REQUEST_AGENT_MODEL=<your-pr-model-id>
UNIT_TESTING_AGENT_MODEL=<your-testing-model-id>

GITHUB_TOKEN=<your-github-or-mcp-token>
```

All of these keys are **required**; if any are missing, `config.get_config_variable` will raise a `ValueError` at import time.
