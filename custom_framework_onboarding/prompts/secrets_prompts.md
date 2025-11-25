---
name: secrets_prompts
description: Onboarding and setup instructions for the Secrets module.
---
### Secrets Module Configuration

**Metadata:**
- **Module**: Secrets
- **Version**: 1.0.0
- **Type**: Security

**Dependencies:**
- None

**Configuration Steps:**
1. Add the Maven dependency.
2. Configure the secrets source in `application.properties`.
3. Inject `SecretsManager` into your components.

**Boilerplate Code:**
Reference the sample project root: `sample_project/`

**Configuration Properties:**
Reference the properties in: `sample_project/src/main/resources/application.properties`
```properties
secrets.source=ENV
```

**Dependency (Maven):**
```xml
<dependency>
    <groupId>test.sample.project</groupId>
    <artifactId>secrets-manager</artifactId>
    <version>1.0.0</version>
</dependency>
```

**Instruction:**
Strictly follow the module details above and do not assume any external configurations.

**Code Comments:**
- Add comments explaining secrets configuration and security practices
- Document injection patterns and validation logic
- Include warnings about secret handling and error cases