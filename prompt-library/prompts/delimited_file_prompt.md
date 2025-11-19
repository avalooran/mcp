# Delimited File Table Formatter

Format delimited file content as a structured table.

## Input
- File path: {file_path}

## Requirements
- Table name: "what a wow"
- Parse delimited data into rows and columns
- Identify headers if present
- Handle different delimiter types

## Output Format
```
Table: what a wow

| Column1 | Column2 | Column3 | ... |
|---------|---------|---------|-----|
| Value1  | Value2  | Value3  | ... |
| Value1  | Value2  | Value3  | ... |
```

## Instructions
- Auto-detect delimiter type
- Use first row as headers if applicable
- Format as markdown table
- Show all records
- Handle missing values gracefully