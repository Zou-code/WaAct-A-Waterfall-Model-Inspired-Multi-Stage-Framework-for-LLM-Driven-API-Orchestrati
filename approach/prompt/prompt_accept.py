

def prompt_accept(requirement, requirement_gherkin, response):
    prompt = '''\
You are a software tester performing acceptance validation.
You are given:
A user requirement in natural language
The same requirement expressed in Gherkin format
A system response from an API or application

Your task:
Determine whether the response fully satisfies the requirement, using both the natural language and Gherkin formats for judgment.

Input:
Requirement:
{{requirement}}

Gherkin Format:
{{requirement_gherkin}}

Response:
{{response}}

Output Format:
Return a JSON object in the following format:
```json
{
  "accepted": true or false,
  "reason": "If not accepted, provide a brief explanation here. If accepted, this can be null."
}
```
If the response is valid and fully satisfies the requirement, return:
```json
{
  "accepted": true,
  "reason": null
}
```
    '''
    prompt = prompt.replace("{{requirement}}", requirement)
    prompt = prompt.replace("{{requirement_gherkin}}", requirement_gherkin)
    prompt = prompt.replace("{{response}}", response)
    return prompt
