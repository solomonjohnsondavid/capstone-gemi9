from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from agent.src.config.config import GITHUB_TOKEN

github_tools = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://api.githubcopilot.com/mcp/",
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "X-MCP-Toolsets": "all",
            "X-MCP-Readonly": "false",
        },
    ),
    tool_filter=[
        'get_me',
        'list_commits',
        'get_commit',
        'get_file_contents',
        'list_branches',
        'create_branch',
        'create_or_update_file',
        'create_pull_request'
    ]
)

github_tools_unit_testing = McpToolset(
    connection_params=StreamableHTTPServerParams(
        url="https://api.githubcopilot.com/mcp/",
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "X-MCP-Toolsets": "all",
            "X-MCP-Readonly": "false",
        },
    ),
    tool_filter=[
        'get_me',
        'search_repositories',
        'get_repository_tree',
        'get_file_contents',
        'list_branches',
        'create_branch',
        'push_files',
    ]
)