instruction = """You are a unit test generation expert.

Generate comprehensive unit tests for this file:

File: {file_path}
Language: {language}

Source Code:
```
{file_info_content}
```

Generate complete unit test file with:
1. All necessary imports
2. Test fixtures/setup if needed
3. Test cases for each function/method
4. Edge cases and error scenarios
5. Proper assertions

Follow {language} best practices:
- Python: pytest with fixtures and parametrize
- JavaScript: Jest or Mocha
- Java: JUnit 5
- Go: testing package

Output ONLY the complete test file content.
Store result with test file path: {test_path}
"""