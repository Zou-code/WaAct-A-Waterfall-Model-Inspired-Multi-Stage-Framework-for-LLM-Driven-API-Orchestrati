# school:JXNU
# author:zouzhou
# createTime: 2025/5/12 19:00

from prompt.prompt_code_generation import prompt_code_generation
import yaml
from util.llm_util import LLM_util
import subprocess
from util.API_documentation_util import API_util
import re

class Implementation:
    def __init__(self, API_type):
        """
        :param API_type: 表示使用的API的类型，有三种方式： tmdb, spotify, Python
        """
        with open('../config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        self.tmdb_API = config["API Key"]["tmdb"]
        self.spotify_API = config["API Key"]["spotify"]
        self.API_type = API_type
        self.llm = LLM_util()
        self.api_util = API_util()
        pass

    def code_generation(self, task_plan, requirement, requirement_gherkin, pseudocode):
        API_key = ''
        server_url = ''
        type = ''
        if self.API_type == "tmdb":
            API_key = self.tmdb_API
            server_url = 'https://api.themoviedb.org/3'
            type = 'rest'
        elif self.API_type == "spotify":
            API_key = self.spotify_API
            type = 'rest'
            server_url = ''

        API_documentation = self.api_util.get_documentation_implementation(task_plan, self.API_type)

        prompt = prompt_code_generation(requirement, API_documentation, pseudocode, API_key, type, server_url, requirement_gherkin)
        executable_code = self.llm.model_deepseek_coder(prompt)
        executable_code = re.sub(r'^```python\n|\n```$', '', executable_code, flags=re.MULTILINE)
        return executable_code

    def run_code(self, executable_code):
        """
        将生成的可运行代码写入到文件中，并执行
        :param executable_code:
        :return:
        """
        with open('./executable_code.py', 'w', encoding='utf-8') as f:
            f.write(executable_code)
            f.flush()
            f.close()

        result = subprocess.run(
            ["python", "./executable_code.py"],
            stdout=subprocess.PIPE,  # 捕获标准输出
            stderr=subprocess.PIPE,  # 捕获标准错误
            text=True,  # 以文本模式读取输出
            encoding='utf-8'  # 指定编码方式为 UTF-8
        )
        return result
