from fastmcp import FastMCP
from mcp.types import PromptMessage, TextContent

mcp = FastMCP("Log Framework Integration")

@mcp.tool()
def ping() -> str:
    """A simple health check tool to ensure the MCP server is loaded."""
    return "MCP server is running"

def get_framework_url(use_github: bool = True) -> str:
    """Returns the framework code location - GitHub URL or local path."""
    return "https://github.com/avalooran/welog" if use_github else "C:\\Users\\User1\\Project\\DEMO\\welog"

@mcp.prompt
def build_sample_app_with_logging_local(folder_path: str, name: str) -> list[PromptMessage]:
    """
    Build a sample application that integrates the existing log framework code.
    
    Args:
        folder_path: Path to the folder containing the log framework code
    """
    framework_url = get_framework_url(use_github=False)
    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"""Build a sample application that integrates the existing log framework code.
                        CONTEXT:
                        - Log framework code is available at: {framework_url}
                        - Need to understand and utilize the framework's logging capabilities

                        REQUIREMENTS:
                        1. Analyze the log framework code to understand:
                        - Available logging methods (debug, info, warn, error, etc.)
                        - Configuration options and initialization requirements
                        - Log output formats and destinations

                        2. Create a sample spring boot application with name {name} under the folder path {folder_path} demonstrating:
                        - Proper initialization of the log framework
                        - Different log levels usage (debug, info, warning, error)
                        - Structured logging with contextual information
                        - Error handling and exception logging
                        - Performance/timing logs where applicable

                        3. Include realistic use cases:
                        - Application startup/shutdown logging
                        - Business logic operations with appropriate log levels
                        - Error scenarios and exception handling
                        - Request/response logging (if applicable)

                        4. Provide documentation:
                        - How to run the sample application
                        - Expected log output examples
                        - Best practices for using the framework

                        DELIVERABLES:
                        - Sample application source code with logging integrated
                        - Configuration files (if required by the framework)
                        - README with setup and execution instructions
                        - Comments explaining logging decisions and patterns

                        INSTRUCTIONS:
                        1. Examine the log framework code at {framework_url} to understand its API and capabilities
                        2. Design a simple but representative application scenario
                        3. Implement the application with comprehensive logging
                        4. Test to ensure logs are generated correctly
                        5. Document the integration approach

                        Please provide a complete sample application with integrated logging."""
            )
        )
    ]


@mcp.prompt
def build_sample_app_with_logging(folder_path: str, name: str) -> list[PromptMessage]:
    """
    Build a sample application that integrates the existing log framework code.
    
    Args:
        folder_path: Path to the folder containing the log framework code
    """
    framework_url = get_framework_url(use_github=True)
    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"""Build a sample application that integrates the existing log framework code.
                        CONTEXT:
                        - Log framework code is available at: {framework_url}
                        - Checkout the framework code to the {folder_path}/framework and use this directory for reference and implementation
                        - Need to understand and utilize the framework's logging capabilities

                        REQUIREMENTS:
                        1. Analyze the log framework code from the folder path {folder_path}/framework to understand:
                        - Available logging methods (debug, info, warn, error, etc.)
                        - Configuration options and initialization requirements
                        - Log output formats and destinations

                        2. Create a sample spring boot application with name {name} under the folder path {folder_path} demonstrating:
                        - Proper initialization of the log framework
                        - Different log levels usage (debug, info, warning, error)
                        - Structured logging with contextual information
                        - Error handling and exception logging
                        - Performance/timing logs where applicable

                        3. Include realistic use cases:
                        - Application startup/shutdown logging
                        - Business logic operations with appropriate log levels
                        - Error scenarios and exception handling
                        - Request/response logging (if applicable)

                        4. Provide documentation:
                        - How to run the sample application
                        - Expected log output examples
                        - Best practices for using the framework

                        DELIVERABLES:
                        - Sample application source code with logging integrated
                        - Configuration files (if required by the framework)
                        - README with setup and execution instructions
                        - Comments explaining logging decisions and patterns

                        INSTRUCTIONS:
                        1. Examine the log framework code at {framework_url} to understand its API and capabilities
                        2. Design a simple but representative application scenario
                        3. Implement the application with comprehensive logging
                        4. Test to ensure logs are generated correctly
                        5. Document the integration approach

                        Please provide a complete sample application with integrated logging."""
            )
        )
    ]

@mcp.prompt
def build_sample_app_with_logging_it1(folder_path: str, name: str) -> list[PromptMessage]:
    """
    Build a sample application that integrates the existing log framework code.
    
    Args:
        folder_path: Path to the folder containing the log framework code
    """
    framework_url = get_framework_url(use_github=True)
    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                 text=f"""Build a sample application that integrates the existing log framework code.
                        CONTEXT:
                        - Log framework code is available at: {framework_url}
                        - Checkout the framework code to the {folder_path}/framework and use this directory for reference and implementation
                        - Need to understand and utilize the framework's logging capabilities

                        REQUIREMENTS:
                        1. Analyze the log framework code from the folder path {folder_path}/framework to understand:
                        - Available logging methods (debug, info, warn, error, etc.)
                        - Configuration options and initialization requirements
                        - Log output formats and destinations

                        2. Create a sample spring boot application with name {name} under the folder path {folder_path} demonstrating:
                        - Proper initialization of the log framework
                        - Different log levels usage (debug, info, warning, error)
                        - Structured logging with contextual information
                        - Error handling and exception logging
                        - Performance/timing logs where applicable

                        3. Include realistic use cases:
                        - Application startup/shutdown logging
                        - Business logic operations with appropriate log levels
                        - Error scenarios and exception handling
                        - Request/response logging (if applicable)

                        4. Provide documentation:
                        - How to run the sample application
                        - Expected log output examples
                        - Best practices for using the framework

                        DELIVERABLES:
                        - Sample application source code with logging integrated
                        - Configuration files (if required by the framework)
                        - README with setup and execution instructions
                        - Comments explaining logging decisions and patterns

                        INSTRUCTIONS:
                        1. Examine the log framework code at {framework_url} to understand its API and capabilities
                        2. Design a simple but representative application scenario
                        3. Implement the application with comprehensive logging
                        4. Test to ensure logs are generated correctly
                        5. Document the integration approach

                        Please provide a complete sample application with integrated logging.
                    """
            )
        )
    ]

if __name__ == "__main__":
    mcp.run()