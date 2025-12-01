from google.adk.agents import LlmAgent
from agent.src.tools.github_tools import github_tools as github_tools_unit_testing
from agent.src.prompts.commit_prompt import instruction

commit_agent = LlmAgent(
        model='gemini-2.5-flash',
        name='CommitAgent',
        description='Commits generated test files to repository',
        instruction=instruction,
        tools=[github_tools_unit_testing],
        output_key='commit_result'
    )