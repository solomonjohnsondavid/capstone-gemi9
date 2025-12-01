from typing import Any, Dict, List, Optional, Union
from google.adk.agents import LlmAgent
from pydantic import BaseModel, RootModel
from agent.src.tools.github_tools import github_tools as github_tools_unit_testing
from agent.src.config.config import REPO_ANALYZER_AGENT_NAME, REPO_ANALYZER_AGENT_MODEL
from agent.src.prompts.repo_analyzer_prompt import instruction

class repo_analyzer_agent_output(BaseModel):
    path: str
    content: str
    language: str

class list_of_repo_analyzer_agent_output(RootModel[Optional[List[repo_analyzer_agent_output]]]):
    """Allow either a list of outputs or None (optional)."""
    pass

def after_tool_callback(
    tool,
    args: Dict[str, Any],
    tool_context,
    tool_response: Dict
) -> Optional[Dict]:
    """
    Called after tool execution.
    Handles special case for get_file_contents to extract text properly.
    """
    print(f"✅ Tool Complete: {tool.name}")
    
    # Special handling for get_file_contents
    if tool.name == "get_file_contents":
        try:
            # Extract text from resource type content
            result = tool_response.get("result", {})
            content_items = result.get("content", [])
            
            # Find the resource item (usually index 1)
            file_text = None
            for item in content_items:
                if isinstance(item, dict) and item.get("type") == "resource":
                    resource = item.get("resource", {})
                    file_text = resource.get("text", "")
                    break
            
            if file_text is not None:
                # Return simplified response with just the text
                return {
                    "result": {
                        "content": file_text,
                        "path": args.get("path", ""),
                        "sha": result.get("sha", "")
                    }
                }
            else:
                print(f"Warning: Could not extract text from resource for {args.get('path')}")
                return {
                    "result": {
                        "content": "",
                        "path": args.get("path", ""),
                        "error": "Failed to extract text content"
                    }
                }
        except Exception as e:
            print(f"Error extracting file content: {e}")
            return {
                "result": {
                    "content": "",
                    "path": args.get("path", ""),
                    "error": str(e)
                }
            }
    
    # For other tools, return None (use original response)
    return None

repo_analyzer_agent = LlmAgent(
        model=REPO_ANALYZER_AGENT_MODEL,
        name=REPO_ANALYZER_AGENT_NAME,
        description='Analyzes repository and identifies files needing unit tests',
        instruction=instruction,
        tools=[github_tools_unit_testing],
        output_key='files_to_test',
        output_schema=list_of_repo_analyzer_agent_output,
        after_tool_callback=after_tool_callback
    )