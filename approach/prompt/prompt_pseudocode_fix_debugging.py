def prompt_pseudocode_fix_debugging(requirement, requirement_gherkin, pseudocode, executable_code, error_message, error_description, api_docs):
    prompt = '''\
You are a senior system designer and software architect.

You are given the following information:
- A natural language **user requirement**
- A **Gherkin specification** (Given-When-Then format) that defines the expected behavior
- The **pseudocode** that was originally written to satisfy the requirement
- The **generated Python code** from that pseudocode
- A **runtime error message** indicating a failure during code execution
- A set of **API documentation entries**

---

## Your task:

Revise the **pseudocode** to fix the **design-level mistake** that caused the code to fail at runtime.

In particular:
- The pseudocode may contain an **incorrectly selected API**, **wrong API usage**, or a **flawed logic flow**
- Your job is to identify and **fix the root cause** in the pseudocode
- You may choose to:
  - Replace the API with a better one from the docs
  - Change how the API is called (e.g., different parameters, options, input structure)
  - Fix the logical steps to match what the runtime requires

You do not need to produce runnable code.
You only need to return a corrected version of the **pseudocode** that is:
- Aligned with the original requirement and Gherkin specification
- Free from design errors that would cause runtime failure

User Requirement:
{user_requirement}

Gherkin Specification:
{requirement_gherkin}

Current Pseudocode:
{pseudocode}

Generated Python Code:
{executable_code}

Runtime Error Message:
{error_message}

Error Description:
{error_description}


API Documentation:
{API_docs}

Return only the revised **pseudocode**, without any explanation or comments.

Make sure the new pseudocode:
- Corrects the mistake that caused the runtime failure
- Remains logically coherent and complete
- Uses appropriate APIs and proper usage patterns as defined in the documentation
- Matches the intent of the original user requirement and Gherkin steps
'''
    prompt = prompt.replace("{user_requirement}", requirement).replace(
        "{requirement_gherkin}", requirement_gherkin).replace(
        "{pseudocode}", pseudocode).replace(
        "{executable_code}", executable_code).replace(
        "{error_message}", error_message).replace(
        "{error_description}", error_description).replace("{API_docs}", api_docs)
    return prompt