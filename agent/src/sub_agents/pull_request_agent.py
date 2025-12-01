from google.adk.agents import LlmAgent

from agent.src.config import config
from agent.src.prompts.pull_request_prompt import instruction
from agent.src.tools.github_tools import github_tools

pull_request_agent = LlmAgent(
    name=config.PULL_REQUEST_AGENT_NAME,
    model=config.PULL_REQUEST_AGENT_MODEL,
    instruction=instruction,
    tools=[github_tools],
)
