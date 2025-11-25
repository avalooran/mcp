---
name: logger_prompts
description: Onboarding and setup instructions for the Logger module.
---
### Logger Module Configuration

**Metadata:**
- **Module**: Logger
- **Version**: 1.0.0
- **Type**: Core Utility

**Dependencies:**
- None

**Configuration Steps:**
1. Add the Maven dependency.
2. Configure logging levels in `application.properties`.
3. Inject `Logger` into your components (Service/Controller).

**Boilerplate Code:**
Reference the sample project root: `sample_project/`

**Configuration Properties:**
Reference the properties in: `sample_project/src/main/resources/application.properties`
```properties
logger.level=INFO
logger.format=JSON
```

**Dependency (Maven):**
```xml
<dependency>
    <groupId>test.sample.project</groupId>
    <artifactId>logger</artifactId>
    <version>1.0.0</version>
</dependency>
```



**Instruction:**
Strictly follow the module details above and do not assume any external configurations.

**Code Comments:**
- Add comments explaining logger configuration properties
- Document injection patterns and usage examples
- Include comments for log levels and formatting choices