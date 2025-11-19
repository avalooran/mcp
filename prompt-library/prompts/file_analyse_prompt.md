# File Type Analysis

Analyze the provided file to determine if it's a delimited file.

## Input
- File path: {file_path}

## Analysis Criteria
Check for:
- CSV format (comma-separated)
- TSV format (tab-separated)
- Pipe-separated values (|)
- Semicolon-separated values (;)
- Other consistent delimiters

## Output
Return one of:
- "DELIMITED" - if file contains structured delimited data
- "NOT_DELIMITED" - if file is plain text, code, or other format

## Instructions
- Read the first few lines to identify patterns
- Look for consistent column separators
- Consider header rows
- Ignore empty lines or comments