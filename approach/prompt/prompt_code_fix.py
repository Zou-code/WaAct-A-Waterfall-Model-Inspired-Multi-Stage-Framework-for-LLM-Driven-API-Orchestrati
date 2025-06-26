
def prompt_code_fix(requirement, requirement_gherkin, executable_code, error_message, error_description, API_docs):
    prompt = '''\
You are an experienced Python developer and software debugger.

You are given:
- A natural language **user requirement**
- A structured **Gherkin specification** that defines the expected behavior
- A **Python implementation** that was generated from pseudocode
- A **runtime error message** indicating failure during execution
- An **error description** from a prior error analysis step, identifying the problem as an **Implementation Layer** issue
- One or more **API documentation entries** relevant to the logic

---

## Your task:

Fix the **Python code** so that:
- It executes without runtime errors
- It aligns with the intent of the **user requirement** and **Gherkin behavior**
- It uses the appropriate APIs correctly (parameters, usage patterns, etc.)
- It preserves the core logic that was intended by the original pseudocode, modifying only what is necessary to correct the implementation mistake

---

## Input

User Requirement:
{{requirement}}

Gherkin Specification:
{{requirement_gherkin}}

Python Code (with runtime error):
{{executable_code}}

Runtime Error Message:
{{error_message}}

Error Description (from error analysis):
{{error_description}}

API Documentation:
{{API_docs}}

## Output Format

Return only the **corrected Python code**.

Ensure:
- The fix is minimal but sufficient to make the code run correctly
- The code reflects the correct logic expected by the user and the Gherkin specification
- All API calls are valid and correctly used (check documentation)

```python
{fixed_code}
```
'''
    prompt = prompt.replace("{{requirement}}", requirement).replace(
        "{{requirement_gherkin}}", requirement_gherkin).replace(
        "{{executable_code}}", executable_code).replace(
        "{{error_message}}", error_message).replace(
        "{{error_description}}", error_description).replace("{{API_docs}}", API_docs)
    return prompt
