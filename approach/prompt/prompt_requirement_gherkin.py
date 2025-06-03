
def prompt_requirement_gherkin(requirement):
    prompt = """\
You are an expert in behavior-driven development (BDD). Given the following user requirement:

{{USER_REQUIREMENT}}

Rewrite it in clear, valid Gherkin syntax using English. Use the standard structure of "Feature", "Scenario", "Given", "When", and "Then". Be concise, \
accurate, and reflect the user's intent faithfully. Only return the Gherkin code block, no explanations.\
"""
    prompt = prompt.replace("{{USER_REQUIREMENT}}", requirement)
    return prompt