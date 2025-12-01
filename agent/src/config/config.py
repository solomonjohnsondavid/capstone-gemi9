from dotenv import load_dotenv
import os

load_dotenv()


def get_config_variable(key: str) -> str:
    """
    Validates a configuration variable and returns its value.

    Args:
        key (str): The name of the configuration variable.

    Returns:
        The value of the configuration variable.

    Raises:
        ValueError: If the variable is not set.
    """
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Missing configuration variable: {key}")
    return value


# Agent Configuration
ORCHESTRATOR_AGENT_NAME = get_config_variable("ORCHESTRATOR_AGENT_NAME")
PULL_REQUEST_AGENT_NAME = get_config_variable("PULL_REQUEST_AGENT_NAME")
UNIT_TESTING_AGENT_NAME = get_config_variable("UNIT_TESTING_AGENT_NAME")

ORCHESTRATOR_AGENT_MODEL = get_config_variable("ORCHESTRATOR_AGENT_MODEL")
PULL_REQUEST_AGENT_MODEL = get_config_variable("PULL_REQUEST_AGENT_MODEL")
UNIT_TESTING_AGENT_MODEL = get_config_variable("UNIT_TESTING_AGENT_MODEL")

# Github Configuration
GITHUB_TOKEN = get_config_variable("GITHUB_TOKEN")
