from prompt.prompt_pseudocode_fix_acceptance import prompt_pseudocode_fix_acceptance
from prompt.prompt_pseudocode_fix_debugging import prompt_pseudocode_fix_debugging
import re
from util.llm_util import LLM_util
from prompt.prompt_error_analysis import prompt_error_analysis
from prompt.prompt_code_fix import prompt_code_fix
class Debugging:
    def __init__(self):
        self.llm = LLM_util()

    def pseudocode_fix_acceptance(self, requirement, requirement_gherkin, pseudocode, failure_reason, response, API_documentation):
        # »ñÈ¡APIÎÄµµ

        prompt = prompt_pseudocode_fix_acceptance(requirement, requirement_gherkin, pseudocode, failure_reason, response, API_documentation)
        fixed_pseudocode = self.llm.model_deepseek_coder(prompt)
        return fixed_pseudocode

    def error_analysis(self, requirement, requirement_gherkin, pseudocode, executable_code, error_message, API_documentation):
        prompt = prompt_error_analysis(requirement, requirement_gherkin, pseudocode, executable_code,error_message, API_documentation)
        error_report = self.llm.model_deepseek_chat(prompt)
        # error_report = re.sub(r'^```python\n|\n```$', '', executable_code, flags=re.MULTILINE)
        error_report = re.sub(r'^```json\s*|\s*```$', '', error_report, flags=re.MULTILINE)
        return error_report

    def pseudocode_fix_debugging(self, requirement, requirement_gherkin, pseudocode, executable_code, error_message, error_description,API_documentation):
        prompt = prompt_pseudocode_fix_debugging(requirement, requirement_gherkin, pseudocode, executable_code,error_message, error_description, API_documentation)
        fixed_pseudocode = self.llm.model_deepseek_coder(prompt)
        return fixed_pseudocode

    def code_fix(self, requirement, requirement_gherkin, executable_code, error_message, error_description, API_docs):
        prompt = prompt_code_fix(requirement, requirement_gherkin, executable_code, error_message, error_description, API_docs)
        fixed_code = self.llm.model_deepseek_coder(prompt)
        fixed_code = re.sub(r'^```python\n|\n```$', '', fixed_code, flags=re.MULTILINE)
        return fixed_code
