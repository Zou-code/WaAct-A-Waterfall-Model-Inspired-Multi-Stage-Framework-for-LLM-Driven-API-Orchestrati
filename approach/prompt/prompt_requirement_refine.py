

def prompt_requirement_refine(requirement, clarification_questions):
    prompt = '''\
You are a system analyst.
You are given:
A natural language user requirement
A list of clarification questions related to that requirement (based on aspects like event, status, type, purpose, condition)

user requirement:
{{requirement}}

clarification questions:
{{clarification_questions}}

Your task:
Carefully review the clarification questions.
For each question, infer a reasonable answer based on context or general logic.
Based on these inferred answers, rewrite and expand the original requirement to be:
Clear and unambiguous
Logically complete
Suitable for implementation

Output Instruction:
Only output the final rewritten requirement
Do not include any answers or intermediate reasoning

rewritten requirement:
```
{rewritten_requirement}
```'''
    prompt = prompt.replace("{{requirement}}", requirement).replace("{{clarification_questions}}", clarification_questions)
    return prompt