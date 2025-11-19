# Custom Promptz MCP Server

A custom MCP server using FastMCP v2 that provides access to local prompt library via FastAPI backend.

## Architecture

```
Amazon Q Developer → FastMCP Server → FastAPI Backend → Local MD Files
```

## Components

1. **FastAPI Backend** (`api/`) - Serves prompts from local markdown files
2. **FastMCP Server** (`mcp-server/`) - MCP server using FastMCP v2
3. **Prompt Library** (`prompt-library/prompts/`) - Local markdown prompt files

## Setup

### 1. Install Dependencies

```bash
# API dependencies
cd api
pip install -r requirements.txt

# MCP server dependencies  
cd ../mcp-server
pip install -r requirements.txt
```

### 2. Start FastAPI Backend

```bash
# Option 1: Use batch file
start_api.bat

# Option 2: Manual start
cd api
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Configure MCP Client

Add to your `~/.aws/amazonq/mcp.json`:

```json
{
  "mcpServers": {
    "custom-promptz": {
      "command": "python",
      "args": ["C:/Users/User1/projects/mcp_server/promptz-dev/custom-promptz-mcp/mcp-server/server.py"],
      "env": {
        "CUSTOM_PROMPTZ_API_URL": "http://localhost:8000"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Available Tools

- `list_prompts(tags=None, nextToken=None)` - List available prompts
- `get_prompt(name)` - Get specific prompt by name

## Usage Examples

- "List all prompts"
- "Get the File Analysis prompt"
- "Use the Delimited File Table Formatter prompt"

## API Endpoints

- `GET /` - API info
- `GET /search-prompts?tags=[]` - Search prompts
- `GET /list-by-name?name=<name>` - Get prompt by name