# Logger Module Rules

**Injection Pattern:**
- Use constructor injection for Logger dependency
- Logger should be final field in service classes

**Usage Standards:**
- Log at INFO level for business operations
- Log at ERROR level for exceptions
- Include relevant context in log messages

**Configuration:**
- Always set logger.level in application.properties
- Use JSON format for structured logging

**Documentation Standards:**
- Comment configuration properties with purpose and valid values
- Document logger injection and usage patterns
- Explain log level choices and formatting decisions