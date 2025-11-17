from fastmcp import FastMCP
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent

# This is the shared MCP server instance
mcp = FastMCP("mcp_prompt_local")

@mcp.prompt
def analyze_data_file(file_path: str, analysis_type: str = "summary") -> list[PromptMessage]:
    """
    Generate a prompt for analyzing data files (CSV/Parquet).

    Args:
        file_path: Path to the data file
        analysis_type: Type of analysis (summary, quality, structure)
    """

    analysis_prompts = {
        "summary": f"Analyze the data file at '{file_path}' and provide a comprehensive summary including:\n- Data dimensions (rows/columns)\n- Column types and names\n- Sample data preview\n- Basic statistics",

        "quality": f"Perform a data quality assessment on '{file_path}':\n- Check for missing values\n- Identify duplicates\n- Detect outliers\n- Validate data types\n- Report data quality score",

        "structure": f"Examine the structure of '{file_path}' and describe:\n- Schema definition\n- Data relationships\n- Column dependencies\n- Recommended optimizations"
    }

    prompt_text = analysis_prompts.get(analysis_type, analysis_prompts["summary"])

    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=prompt_text
            )
        )
    ]

@mcp.prompt
def compare_data_files(file1: str, file2: str) -> list[PromptMessage]:
    """
    Generate a prompt for comparing two data files.

    Args:
        file1: Path to first data file
        file2: Path to second data file
    """

    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"Compare the data files '{file1}' and '{file2}':\n"
                     f"- Schema differences\n"
                     f"- Data volume comparison\n"
                     f"- Common/unique columns\n"
                     f"- Data type mismatches\n"
                     f"- Recommendations for data harmonization"
            )
        )
    ]

@mcp.prompt
def generate_data_processing_plan(file_path: str, target_format: str = "parquet") -> list[PromptMessage]:
    """
    Generate a prompt for creating data processing workflows.

    Args:
        file_path: Source data file path
        target_format: Target format (parquet, csv, json)
    """

    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"Create a data processing plan for '{file_path}' to convert to {target_format}:\n"
                     f"- Analyze current data structure\n"
                     f"- Identify transformation requirements\n"
                     f"- Suggest optimization strategies\n"
                     f"- Provide step-by-step conversion process\n"
                     f"- Include validation steps"
            )
        )
    ]

# Entry point to run the server
if __name__ == "__main__":
    # For remote deployment, use HTTP
    #mcp.run(transport="sse")  # Server-Sent Events over HTTP

    #For local server,
    mcp.run() #Don't start the server. Rather use any client to handle