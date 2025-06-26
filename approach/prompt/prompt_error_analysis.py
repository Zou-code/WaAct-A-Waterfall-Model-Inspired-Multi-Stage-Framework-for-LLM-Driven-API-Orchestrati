def prompt_error_analysis(requirement, requirement_gherkin, pseudocode, executable_code, error_message, API_docs):
    prompt = '''\
You are an expert software engineer and debugging analyst.

You are given:
- A **natural language user requirement**
- A **Gherkin-style behavior specification**
- A **pseudocode implementation**, meant to fulfill the requirement
- A **generated Python code** from that pseudocode
- A **runtime error message**
- One or more **API documentation entries**


## Your task:

Analyze the error and determine where the root cause lies. The error can be in one of the following categories:

### Design Layer (Pseudocode-Level Mistake)
This means the pseudocode itself is flawed. Possible causes include:
- Incorrect API Selection**: The API used in the pseudocode does not meet the actual need.
- Incorrect API Usage Pattern**: The API is generally correct, but used in the wrong way (e.g., wrong parameters or assumptions).
- Logical Flaw**: The sequence or logic of operations doesn't match the requirement or Gherkin steps.

### Implementation Layer (Code Generation Mistake)
This means the Python code is incorrect **despite the pseudocode being valid**. Possible causes include:
- Incorrect syntax
- Incorrect translation of steps
- Misused variables, formatting issues, or API misapplication that was not present in the pseudocode

---

## Input

User Requirement:
{{requirement}}

Gherkin Specification:
{{requirement_gherkin}}

Pseudocode:
{{pseudocode}}

Python Code:
{{executable_code}}

Runtime Error Message:
{{error_message}}

API Documentation:
{{API_docs}}

## Output Format
Respond only with a JSON object like the following:

```json
{
  "error_aspect": "Design",  // or "Implementation"
  "error_description": "Explain the reason for the error. Include your analysis and reference to pseudocode or code. Be specific: was it a wrong API? A logic flaw? A code-level syntax issue? Make your reasoning clear and justified."
}
'''
    prompt = prompt.replace("{{requirement}}", requirement).replace(
        "{{requirement_gherkin}}", requirement_gherkin).replace(
        "{{pseudocode}}", pseudocode).replace(
        "{{executable_code}}", executable_code).replace(
        "{{error_message}}", error_message).replace("{{API_docs}}", API_docs)
    return prompt