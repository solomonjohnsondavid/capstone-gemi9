from google.adk.agents.llm_agent import LlmAgent

from agent.src.config import config
from agent.src.prompts.unit_testing_prompt import instruction

unit_testing_agent = LlmAgent(
    name=config.PULL_REQUEST_AGENT_NAME,
    model=config.PULL_REQUEST_AGENT_MODEL,
    instruction=instruction,
)
