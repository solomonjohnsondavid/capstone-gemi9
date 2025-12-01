from google.adk.agents.sequential_agent import SequentialAgent
from agent.src.sub_agents.repo_analyzer_agent import repo_analyzer_agent as repo_analyzer
from agent.src.sub_agents.unit_parallel_agent import dynamic_parallel_generator_agent as dynamic_parallel_generator
from agent.src.sub_agents.commit_agent import commit_agent

unit_testing_agent = SequentialAgent(
    name='UnitTestGenerationPipeline',
    description=f'Generates unit tests',
    sub_agents=[
        repo_analyzer,           # Step 1: Analyze repo
        dynamic_parallel_generator,  # Step 2: Generate tests in parallel
        commit_agent             # Step 3: Commit tests
    ]
)