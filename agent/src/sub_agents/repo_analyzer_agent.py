from typing import List
from google.adk.agents import LlmAgent
from pydantic import BaseModel
from agent.src.tools.github_tools import github_tools as github_mcp_toolset
from agent.src.config.config import REPO_ANALYZER_AGENT_NAME, REPO_ANALYZER_AGENT_MODEL
from agent.src.prompts.repo_analyzer_prompt import instruction

class repo_analyzer_agent_output(BaseModel):
    path: str
    content: str
    language: str

repo_analyzer_agent = LlmAgent(
        model=REPO_ANALYZER_AGENT_MODEL,
        name=REPO_ANALYZER_AGENT_NAME,
        description='Analyzes repository and identifies files needing unit tests',
        instruction=instruction,
        tools=[github_mcp_toolset],
        output_key='files_to_test',
        output_schema=List[repo_analyzer_agent_output],
    )