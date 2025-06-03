# school:JXNU
# author:zouzhou
# createTime: 2025/5/12 15:47

from prompt.prompt_requirement_gherkin import prompt_requirement_gherkin
from prompt.prompt_clarifying_question_generation import prompt_clarifying_question_generation
from prompt.prompt_requirement_refine import prompt_requirement_refine
import re
from util.llm_util import LLM_util

class RequirementAnalysis:
    def __init__(self):
        self.llm = LLM_util()
        pass

    def clarifying_question_generation(self,requirement):
        prompt = prompt_clarifying_question_generation(requirement)
        questions = self.llm.model_deepseek_chat(prompt)
        return questions

    def requirement_refine(self,requirement, clarifying_questions):
        prompt = prompt_requirement_refine(requirement, clarifying_questions)
        refined_requirement = self.llm.model_deepseek_chat(prompt)
        return refined_requirement

    def requirement_gherkin(self,requirement):
        # 获取需求
        prompt = prompt_requirement_gherkin(requirement)
        # 调用大模型分析需求
        result = self.llm.model_deepseek_chat(prompt)
        return result

    def requirement_run(self, requirement):
        clarifying_questions = self.clarifying_question_generation(requirement)
        clarifying_questions = re.sub(r'^```json\s*|\s*```$', '', clarifying_questions, flags=re.MULTILINE)
        if clarifying_questions == 'None':
            requirement_gherkin = self.requirement_gherkin(requirement)
            return requirement, requirement_gherkin
        refined_requirement = self.requirement_refine(requirement, clarifying_questions)
        requirement_gherkin = self.requirement_gherkin(refined_requirement)
        return refined_requirement, requirement_gherkin


if __name__ == '__main__':
    ra = RequirementAnalysis()
    requirement = "Give me the number of movies directed by Sofia Coppola."
    # result = ra.clarifying_question_generation(requirement)
    # requirement = "Count the number of movies where Sofia Coppola is credited as a director (including cases where she is one of multiple directors). The count should include only released or publicly available movies, and the result should be returned as an integer."
    questions = '''
```
1. Should the count include only movies where Sofia Coppola is the sole director, or also movies where she is one of multiple directors?
2. Should the count include all movies directed by Sofia Coppola, or only those that are released or publicly available?
3. Should the count be returned as an integer (e.g., 5) or as a string (e.g., "5 movies")?
```'''

    # questions = ra.clarifying_question_generation(requirement)
    # result = ra.requirement_refine(requirement, questions)
    # print(questions)
    gherkin = ra.requirement_run(requirement)
    print(gherkin)