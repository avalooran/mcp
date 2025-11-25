# Secrets Module Rules

**Security Standards:**
- Always validate secrets exist before use
- Throw RuntimeException for missing critical secrets
- Use ENV as default secrets source

**Injection Pattern:**
- Use constructor injection for SecretsManager
- SecretsManager should be final field

**Error Handling:**
- Log security violations at ERROR level
- Never log actual secret values