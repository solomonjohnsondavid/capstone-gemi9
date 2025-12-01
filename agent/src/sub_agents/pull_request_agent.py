from google.adk.agents.llm_agent import LlmAgent

from agent.src.config import config
from agent.src.tools.github_tools import github_tools
from agent.src.prompts.pull_request_prompt import instruction

pull_request_agent = LlmAgent(
    name=config.PULL_REQUEST_AGENT_NAME,
    model=config.PULL_REQUEST_AGENT_MODEL,
    instruction=instruction,
    tools=[github_tools],
)
