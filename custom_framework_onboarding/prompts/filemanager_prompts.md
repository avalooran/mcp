---
name: filemanager_prompts
description: Onboarding and setup instructions for the File Manager module.
---
### File Manager Module Configuration

**Metadata:**
- **Module**: File Manager
- **Version**: 1.0.0
- **Type**: IO / Storage

**Dependencies:**
- @logger_prompts (Required for logging file operations)
- @secrets_prompts (Required if using Cloud Storage like S3/GCS)

**Configuration Steps:**
1. Add the Maven dependency.
2. Configure storage settings in `application.properties`.
3. Inject `FileManager` into your components.

**Boilerplate Code:**
Reference the sample project root: `sample_project/`

**Configuration Properties:**
Reference the properties in: `sample_project/src/main/resources/application.properties`
```properties
filemanager.storage.type=LOCAL
filemanager.base.path=./data
```

**Dependency (Maven):**
```xml
<dependency>
    <groupId>test.sample.project</groupId>
    <artifactId>file-manager</artifactId>
    <version>1.0.0</version>
</dependency>
```



**Instruction:**
Strictly follow the module details above and do not assume any external configurations.

**Code Comments:**
- Add comments explaining file manager configuration and storage options
- Document dependency requirements (Logger and Secrets)
- Include comments for error handling and file operation patterns