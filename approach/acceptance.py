
import json

from prompt.prompt_accept import prompt_accept
from util.llm_util import LLM_util
import re

class Acceptance:
    def __init__(self):
        self.llm = LLM_util()
        pass

    def accept_validation(self, requirement, requirement_gherkin, response):
        prompt = prompt_accept(requirement, requirement_gherkin, response)
        result = self.llm.model_deepseek_chat(prompt)
        result = re.sub(r'^```json\s*|\s*```$', '', result, flags=re.MULTILINE)
        result = json.loads(result)
        accepted = result.get('accepted')
        reason = result.get('reason')
        return accepted, reason