from google.adk.agents.llm_agent import LlmAgent

from agent.src.config import config
from agent.src.prompts.orchestrator_prompt import instruction
from agent.src.sub_agents import pull_request_agent, unit_testing_agent

orchestrator_agent = LlmAgent(
    name=config.ORCHESTRATOR_AGENT_NAME,
    model=config.ORCHESTRATOR_AGENT_MODEL,
    instruction=instruction,
    sub_agents=[pull_request_agent, unit_testing_agent],
)

root_agent = orchestrator_agent
