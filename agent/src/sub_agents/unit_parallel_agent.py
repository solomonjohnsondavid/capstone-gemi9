from google.adk.agents import LlmAgent, ParallelAgent
from typing import Optional, List
from agent.src.sub_agents.test_generator_agent import create_test_generator_agent
from agent.src.config.config import TEST_GENERATOR_AGENT_MODEL

class DynamicParallelTestGeneratorAgent(LlmAgent):
    """
    Custom agent that creates and executes a ParallelAgent dynamically
    based on files_to_test in state.
    """
    
    def __init__(self):
        super().__init__(
            model=TEST_GENERATOR_AGENT_MODEL,
            name='DynamicParallelTestGenerator',
            description='Dynamically creates parallel test generators',
            instruction='This agent dynamically creates parallel test generators',
            tools=[]
        )
        self._parallel_agent: Optional[ParallelAgent] = None
    
    async def run_async(self, invocation_context, new_message=None):
        """
        Override run_async to dynamically create and execute ParallelAgent.
        """
        # Get files_to_test from state
        state = invocation_context.state
        files_to_test = state.get('files_to_test', [])
        
        if not files_to_test:
            print("No files to test found in state")
            return
        
        print(f"\nDynamically creating test generators for {len(files_to_test)} files")
        
        # Create test generator agents dynamically
        test_generator_agents = [
            create_test_generator_agent(file_info)
            for file_info in files_to_test
        ]
        
        # Create ParallelAgent with these sub-agents
        parallel_agent = ParallelAgent(
            name='ParallelTestGenerators',
            description='Generates tests in parallel',
            sub_agents=test_generator_agents
        )
        
        # Execute the parallel agent
        async for event in parallel_agent.run_async(invocation_context, new_message):
            yield event
            
dynamic_parallel_generator_agent = DynamicParallelTestGeneratorAgent()