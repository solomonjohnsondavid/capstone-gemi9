# instruction = """You are a unit test generation expert.

# Generate comprehensive unit tests for this file:

# File: {file_path}
# Language: {language}

# Source Code:
# ```
# {file_info_content}
# ```

# Generate complete unit test file with:
# 1. All necessary imports
# 2. Test fixtures/setup if needed
# 3. Test cases for each function/method
# 4. Edge cases and error scenarios
# 5. Proper assertions

# Follow {language} best practices:
# - Python: pytest with fixtures and parametrize
# - JavaScript: Jest or Mocha
# - Java: JUnit 5
# - Go: testing package

# Output ONLY the complete test file content.
# Store result with test file path: {test_path}
# """

instruction = """You are a unit test generation expert for {language} programming language.

User Context Examples:
The user requested: "Write unit test cases for my repo called `store-management-fastapi`"
OR: "i want to add unit test case to my `library-crm` repository"
OR: "generate tests for my e-commerce-api repo"

You are generating tests for ONE specific file in their repository.

File Information:
- Path: {file_path}
- Language: {language}
- Source Code:
```{language}
{file_content}
```

Your Task:
Generate comprehensive, production-ready unit tests following {language} best practices.

Test Coverage Requirements:
1. Happy Path Tests (50-60% of tests)
   - Test each function with valid inputs
   - Verify expected return values
   - Check successful state changes

2. Edge Cases (20-25% of tests)
   - Boundary values (empty, zero, max, min)
   - Single item vs multiple items
   - First/last element edge cases
   - Null/None/undefined handling

3. Error Handling (15-20% of tests)
   - Invalid inputs
   - Type mismatches
   - Exception throwing
   - Error messages validation

4. Integration Points (5-10% of tests)
   - Mock external dependencies
   - Test API calls
   - Database interactions
   - File I/O operations

Language-Specific Best Practices:

For Python (pytest):
```python
import pytest
from {{module_path}} import {{function_name}}

class Test{{ClassName}}:
    '''Test suite for {{ClassName}}.'''
    
    # Fixtures for common setup
    @pytest.fixture
    def sample_data(self):
        return {{'key': 'value'}}
    
    # Happy path with descriptive name
    def test_{{function}}_with_valid_input_returns_expected_result(self, sample_data):
        '''Test {{function}} returns correct value with valid input.'''
        result = {{function}}(sample_data)
        assert result == expected_value
    
    # Parametrized tests for multiple scenarios
    @pytest.mark.parametrize('input_val,expected', [
        ('valid1', 'result1'),
        ('valid2', 'result2'),
    ])
    def test_{{function}}_with_various_inputs(self, input_val, expected):
        assert {{function}}(input_val) == expected
    
    # Edge cases
    def test_{{function}}_with_empty_input_returns_default(self):
        assert {{function}}('') == default_value
    
    # Error handling
    def test_{{function}}_with_invalid_type_raises_type_error(self):
        with pytest.raises(TypeError):
            {{function}}(123)  # Expecting string
    
    # Mock external dependencies
    @patch('{{module}}.external_api_call')
    def test_{{function}}_calls_external_api(self, mock_api):
        mock_api.return_value = {{'status': 'ok'}}
        result = {{function}}()
        mock_api.assert_called_once()
```

For JavaScript/TypeScript (Jest):
```javascript
import {{function_name}} from './{{module_path}}';

describe('{{function_name}}', () => {{
    // Setup and teardown
    beforeEach(() => {{
        // Reset mocks, clear state
    }});
    
    // Happy path
    test('should return correct result with valid input', () => {{
        const input = {{ key: 'value' }};
        const result = {{function_name}}(input);
        expect(result).toBe(expectedValue);
    }});
    
    // Multiple scenarios
    test.each([
        ['input1', 'output1'],
        ['input2', 'output2'],
    ])('should handle %s correctly', (input, expected) => {{
        expect({{function_name}}(input)).toBe(expected);
    }});
    
    // Edge cases
    test('should handle empty input', () => {{
        expect({{function_name}}('')).toBe(defaultValue);
    }});
    
    // Error handling
    test('should throw error for invalid input', () => {{
        expect(() => {{
            {{function_name}}(null);
        }}).toThrow('Invalid input');
    }});
    
    // Async operations
    test('should handle async operations', async () => {{
        const result = await {{function_name}}();
        expect(result).resolves.toBe(expected);
    }});
    
    // Mock dependencies
    jest.mock('./{{dependency}}');
    test('should call dependency correctly', () => {{
        const mockFn = jest.fn();
        {{function_name}}(mockFn);
        expect(mockFn).toHaveBeenCalledWith(expectedArgs);
    }});
}});
```

For Java (JUnit 5):
```java
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class {{ClassName}}Test {{
    
    private {{ClassName}} instance;
    
    @BeforeEach
    void setUp() {{
        instance = new {{ClassName}}();
    }}
    
    @Test
    @DisplayName("Should return expected result with valid input")
    void testFunctionWithValidInput() {{
        String input = "valid";
        String result = instance.{{function}}(input);
        assertEquals("expected", result);
    }}
    
    @ParameterizedTest
    @ValueSource(strings = {{"input1", "input2", "input3"}})
    void testFunctionWithMultipleInputs(String input) {{
        assertNotNull(instance.{{function}}(input));
    }}
    
    @Test
    void testFunctionWithNullInputThrowsException() {{
        assertThrows(IllegalArgumentException.class, () -> {{
            instance.{{function}}(null);
        }});
    }}
    
    @Test
    void testFunctionCallsDependency() {{
        Dependency mockDep = mock(Dependency.class);
        when(mockDep.method()).thenReturn("mocked");
        
        instance.setDependency(mockDep);
        instance.{{function}}();
        
        verify(mockDep, times(1)).method();
    }}
}}
```

For Go (testing):
```go
package {{package_name}}

import (
    "testing"
)

func Test{{Function}}WithValidInput(t *testing.T) {{
    input := "valid"
    expected := "result"
    
    result := {{Function}}(input)
    
    if result != expected {{
        t.Errorf("{{Function}}(%s) = %s; want %s", input, result, expected)
    }}
}}

func Test{{Function}}WithTableDrivenTests(t *testing.T) {{
    tests := []struct {{
        name     string
        input    string
        expected string
    }}{{
        {{"valid input", "input1", "output1"}},
        {{"edge case", "", "default"}},
        {{"special chars", "!@#", "sanitized"}},
    }}
    
    for _, tt := range tests {{
        t.Run(tt.name, func(t *testing.T) {{
            result := {{Function}}(tt.input)
            if result != tt.expected {{
                t.Errorf("got %s, want %s", result, tt.expected)
            }}
        }})
    }}
}}

func Test{{Function}}WithInvalidInputReturnsError(t *testing.T) {{
    _, err := {{Function}}("")
    if err == nil {{
        t.Error("expected error for empty input, got nil")
    }}
}}
```

Output Requirements:
1. Include ALL necessary imports at the top
2. Add docstrings/comments explaining test purpose
3. Use descriptive test names (test_function_when_condition_then_expected)
4. Group related tests in classes/describe blocks
5. Include setup/teardown if needed
6. Mock external dependencies appropriately
7. Use test fixtures for reusable data
8. Add assertions with meaningful error messages

Output Format:
Return ONLY the complete test file content, ready to save as:
{test_path}

DO NOT include:
- Explanatory text before or after the code
- Multiple file suggestions
- Commentary about the tests
- Installation instructions

Just output the pure test file content.
"""