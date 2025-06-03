

def prompt_pseudocode_generation(requirement,requirement_gherkin,API_documentation):
#     prompt = '''\
# You are a senior software architect. Based on the following three inputs:
# A list of available APIs and their documentation
# The user's natural language requirement
# The same requirement expressed in Gherkin format
# Your task is to generate clear, high-level pseudocode that fulfills the user’s requirement. \
# The pseudocode should represent logical steps that use the available APIs to complete the tasks described.
#
# requirement:
# {{requirement}}
#
# Gherkin Format:
# {{requirement_gherkin}}
#
# API_documentation:
# {{API_documentation}}
#
# Instructions:
# Use only the provided APIs.
# The pseudocode should be structured and readable (e.g., using function calls, conditionals, simple loops if needed).
# Reflect the logical sequence implied by the Gherkin steps.
# Do not output real code in any specific language.
# Return only the pseudocode block, no extra explanations.
# '''
    prompt = '''\
You are a senior software architect.
Based on the following three inputs:
A list of available RESTful APIs and their documentation
The user's requirement written in natural language
The same requirement written in Gherkin format
Your task is to generate clear, high-level pseudocode that logically fulfills the user's requirement using only the provided RESTful APIs.
requirement:
{{requirement}}

Gherkin Format:
{{requirement_gherkin}}

API_documentation:
{{API_documentation}}

Guidelines:
The pseudocode must be modular: define multiple high-level abstract functions，each representing an API interaction or logical step.

Include a main function (or equivalent) that represents the overall orchestration logic.

The pseudocode should be:
Language-neutral
Implementation-agnostic
Highly abstract, avoiding any real names, syntax, or data formats
All logic must follow the structure implied by the Gherkin scenario.
Use only the APIs from the provided documentation.
Output only the pseudocode block, no explanation or extra text.

Output Structure Example (Abstract Pseudocode Format):
```
function Step_A:
    perform an API operation
    return result_X

function Step_B with input result_X:
    perform another API operation
    return result_Y

function Step_C with input result_Y:
    perform additional API operation or transformation
    return result_Z

function Main:
    output_X = Step_A
    output_Y = Step_B using output_X
    output_Z = Step_C using output_Y
    perform final processing or return result
```
'''
    prompt = prompt.replace("{{requirement}}", requirement).replace("{{requirement_gherkin}}", requirement_gherkin).replace("{{API_documentation}}", API_documentation)
    return prompt
