

import yaml
from pathlib import Path
import pandas as pd
import os
from prompt.prompt_task_plan import prompt_task_plan
from prompt.prompt_pseudocode_generation import prompt_pseudocode_generation

from util.llm_util import LLM_util
from util.API_documentation_util import API_util
import re
import json


class Design:
    def __init__(self):
        with open('../config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        # base_dir = Path.cwd()
        # TODO 改善路径的写法
        base_dir = Path(os.getcwd())
        print(base_dir)
        self.path_apis_tmdb = base_dir / config['file path']['apis_tmdb_path']
        self.path_apis_spotify = base_dir / config['file path']['apis_spotify_path']

        self.llm = LLM_util()
        self.df_apis = pd.read_csv("../data/restbench/apis/tmdb.csv")
        pass

    def task_plan(self, requirement, requirement_gherkin):
        API_documentation = ''''''

        for _, row in self.df_apis.iterrows():
            APIs_temp = f'''

endpoint name: {row["endpoint_name"]}
description: {row["endpoint_description"]}
'''
            API_documentation += APIs_temp
        # print(API_documentation)
        prompt = prompt_task_plan(requirement, requirement_gherkin, API_documentation)
        task_plan = self.llm.model_deepseek_chat(prompt)
        return task_plan

    def pseudocode_generation(self, requirement, requirement_gherkin, task_plan):
        API_documentation = API_util.get_documentation_design(task_plan, "tmdb")
        # print(API_documentation)
        prompt = prompt_pseudocode_generation(requirement, requirement_gherkin, API_documentation)
        pseudocode = self.llm.model_deepseek_coder(prompt)
        return pseudocode

    def design_run(self, requirement, requirement_gherkin):
        task_plan = self.task_plan(requirement, requirement_gherkin)
        pseudocode = self.pseudocode_generation(requirement, requirement_gherkin, task_plan)
        return task_plan, pseudocode
