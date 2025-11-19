#!/usr/bin/env python3
import os
import json
import requests
from typing import List, Optional, Dict, Any
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Custom Promptz MCP Server")

# API configuration
API_BASE_URL = os.getenv("CUSTOM_PROMPTZ_API_URL", "http://localhost:8000")

def make_api_request(endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
    """Make request to local FastAPI server"""
    try:
        url = f"{API_BASE_URL}/{endpoint}"
        response = requests.get(url, params=params or {})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"API request failed: {str(e)}")

@mcp.tool()
def list_prompts(tags: Optional[List[str]] = None, nextToken: Optional[str] = None) -> str:
    """List available prompts from the custom prompt library"""
    try:
        params = {}
        if tags:
            params["tags"] = tags
        if nextToken:
            params["nextToken"] = nextToken
        
        response = make_api_request("search-prompts", params)
        
        result = {
            "prompts": [
                {
                    "name": prompt["name"],
                    "description": prompt["description"],
                    "tags": prompt["tags"],
                    "author": prompt.get("author")
                }
                for prompt in response["results"]
            ],
            "nextCursor": response.get("nextToken")
        }
        
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error listing prompts: {str(e)}"

@mcp.tool()
def get_prompt(name: str) -> str:
    """Get a specific prompt by name"""
    try:
        params = {"name": name}
        response = make_api_request("list-by-name", params)
        
        items = response.get("items", [])
        if not items:
            return f"Prompt not found: {name}"
        
        prompt = items[0]
        result = {
            "name": prompt["name"],
            "description": prompt["description"],
            "tags": prompt["tags"],
            "author": prompt.get("author"),
            "instruction": prompt["instruction"],
            "howto": prompt.get("howto", "")
        }
        
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error getting prompt: {str(e)}"

if __name__ == "__main__":
    mcp.run()