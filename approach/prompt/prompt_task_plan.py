

def prompt_task_plan(requirement, requirement_gherkin, available_API):
    prompt = """\
You are a system planner. Given a set of available APIs with descriptions and a user requirement expressed in Gherkin format, your job is to:
Break down the Gherkin-described requirement into a list of clear, actionable sub-tasks.
For each sub-task, identify one "Primary API" and multiple "Alternative APIs" that can fulfill the same or similar functionality.
Only select APIs from the provided list of APIs. Do not invent or assume APIs.
Return your answer strictly as a JSON-formatted string in the following format:
[
  {
    "task": "description of subtask",
    "Primary API": "name_of_primary_api_from_list",
    "Alternative APIs": ["alternative_api_1", "alternative_api_2"]
  }
]
Available APIs:
{{available_API}}
User Requirement (in Gherkin):
{{requirement_gherkin}}
User Requirement (in plain text):
{{requirement}}
Instructions:
Use only the API names from the list provided above.
Keep task descriptions short but meaningful.
Every API entry must be consistent with its described capabilities.
Output only valid JSON. No explanation or comments.\
"""

    prompt = prompt.replace("{{available_API}}", available_API).replace("{{requirement_gherkin}}", requirement_gherkin).replace("{{requirement}}", requirement)
    return prompt
