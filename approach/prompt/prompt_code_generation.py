

def prompt_code_generation(requirement, API_documentation, pseudocode, API_key, type, url, requirement_gherkin):
    if type == "rest":
        prompt = '''
You are a senior backend developer.
You are given:
A natural language description of the user's requirement
A Gherkin description of the user's requirement
A set of RESTful API documentation
A high-level pseudocode representation of the solution logic
An API request key, used for authentication when making API calls
A server url, used for making API calls


Your task:
Convert the given pseudocode into fully functional Python code that fulfills the user’s requirement using the specified APIs.
Use only the provided RESTful APIs as described in the documentation.

User Requirement:
{{requirement}}

Gherkin Format of the User Requirement
{{requirement_gherkin}}

API Documentation:
{{API_documentation}}

Pseudocode:
{{pseudocode}}

API Request Key:
{{api_key}}

server url:
{{url}}


Use Python 3 with standard libraries and, if needed, requests for HTTP calls.
Include the API request key as appropriate in each request (e.g., as query parameter or header, based on the API docs).
Handle common API response behaviors, including:
HTTP method usage (GET, POST, etc.)
Authentication/authorization
Status code checking
Basic error handling (e.g., print/log errors for non-200 responses)
Convert each function in the pseudocode into a corresponding Python function with real request logic.
Ensure the final main() function orchestrates the execution flow according to the pseudocode logic.
Return only the complete Python code block. Do not include explanations or comments outside the code.
'''
        prompt = ((prompt.replace("{{requirement}}", requirement).replace("{{API_documentation}}", API_documentation).
                  replace("{{pseudocode}}", pseudocode).replace("{{api_key}}", API_key)).
                  replace("{{url}}", url).replace("{{requirement_gherkin}}", requirement_gherkin))
        return prompt
    else:
        return
