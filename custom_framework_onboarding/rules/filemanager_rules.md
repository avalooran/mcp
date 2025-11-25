# File Manager Module Rules

**Dependencies:**
- Requires Logger for operation logging
- Requires Secrets if using cloud storage

**Injection Pattern:**
- Use constructor injection for FileManager
- FileManager should be final field

**Error Handling:**
- Wrap file operations in try-catch blocks
- Log file operations at INFO level
- Log failures at ERROR level

**Configuration:**
- Use LOCAL storage type by default
- Set base path for file operations