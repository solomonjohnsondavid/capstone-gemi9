from typing import Dict
from google.adk.agents import LlmAgent
from agent.src.prompts.test_generator_prompt import instruction
from agent.src.config.config import TEST_GENERATOR_AGENT_NAME, TEST_GENERATOR_AGENT_MODEL

def _get_test_file_path(source_path: str, language: str) -> str:
    """Generate test file path based on language conventions."""
    from pathlib import Path
    
    path = Path(source_path)
    stem = path.stem
    
    if language.lower() == 'python':
        return f"tests/test_{stem}.py"
    elif language.lower() in ['javascript', 'typescript']:
        return f"__tests__/{stem}.test{path.suffix}"
    elif language.lower() == 'java':
        return source_path.replace('src/main/java', 'src/test/java').replace('.java', 'Test.java')
    elif language.lower() == 'go':
        return source_path.replace('.go', '_test.go')
    else:
        return f"tests/test_{path.name}"

def create_test_generator_agent(file_info: Dict[str, str]) -> LlmAgent:

    file_path = file_info.get('path', 'unknown')
    language = file_info.get('language', 'unknown')
    
    # Determine test file path
    test_path = _get_test_file_path(file_path, language)
    
    return LlmAgent(
        model=TEST_GENERATOR_AGENT_MODEL,
        name=f'TestGenerator_{file_path.replace("/", "_")}',
        description=f'Generates unit tests for {file_path}',
        instruction=instruction.format(file_path=file_path, test_path=test_path, language=language, file_info_content=file_info.get('content', '')),
        tools=[], 
        output_key=f'test_{file_path.replace("/", "_")}',
    )