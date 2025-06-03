

def prompt_clarifying_question_generation(requirement):
    prompt = '''\
You are a system analyst.
Your task is to review a natural language user requirement and determine whether it contains any ambiguities or missing information that should be clarified before implementation.

user requirement:
{{requirement}}

In Program development, unclear and unambiguous requirements often have multiple APIs that can be implemented, while clear and unambiguous queries can only be implemented by certain specific APIs. \
So in order to be able to get specific API, clarification questions need to be asked for unclear and unambiguous queries.
Below are the meanings of aspect for the query. 
1. event: The action that the query requires. 
2. status: The status of the object that the query requires. The modifier include adjectives, verbs, quantifiers, and adverbs. 
3. type: The type of the object that the query requires. The noun or proper noun is the modifier. The modifier is Python built-in data type, such as "byte", "float", "char", "boolean", "double", etc 
4. purpose: Purpose contains purpose clauses, which are employed to highlight the driving forces behind specific actions. The words "to," "in order to," and "so that" are used to start canonical purpose clauses.
5. condition: The conditio n of the query.

For each unclear or ambiguous aspect above, write several specific clarification question, you should keep your questions concise and focused.
output as the following format:
```
1. {question1}
...
```

If the requirement is fully clear and unambiguous.
output as the following format:
```
None
```

Please note that, you should only output the clarification questions or "None" if the requirement is fully clear and unambiguous in ``` ```., don't output any other words.
'''
    prompt = prompt.replace("{{requirement}}", requirement)
    return prompt