
import json
import re
import pandas as pd
class API_util:

    df_tmdb = pd.read_csv('../data/restbench/apis/tmdb.csv')
    df_spotify = pd.read_csv('../data/restbench/apis/spotify.csv')

    def __init__(self):

        pass

    @staticmethod
    def get_documentation_design(task_plan,API_type):
        """
        根据任务规划列表获取对应的API文档
        :param task_plan: API规划列表，包括API名称和API的参数
        :param API_type: API的类型，用于确定从哪个数据集中获取API文档 分三类：tmdb, spotify 和 Python
        :return:
        """

        df_apis = pd.DataFrame()
        if API_type == "tmdb":
            df_apis = API_util.df_tmdb
        elif API_type == "spotify":
            df_apis = API_util.df_spotify

        # 获取task_plan中的主API,并进行去重
        task_plan = re.sub(r'^```json\s*|\s*```$', '', task_plan, flags=re.MULTILINE)
        task_plan = json.loads(task_plan)
        primary_APIs = set()
        for item in task_plan:
            primary_API = item.get("Primary API")
            if primary_API:
                primary_APIs.add(primary_API)

        API_documentation = ''''''
        for API_name in primary_APIs:
            for _, row in df_apis.iterrows():
                if row["endpoint_name"] == API_name:
                    APIs_temp = f'''

endpoint name: {row["endpoint_name"]}
description: {row["endpoint_description"]}
parameters: {row["parameters"]}'''
                    API_documentation += APIs_temp
        return API_documentation

    @staticmethod
    def get_documentation_implementation(task_plan, API_type):
        """
        根据任务规划列表获取对应的API文档,用于代码生成、Debugging模块的错误分析等
        :param API_type:
        :return:
        """
        df_apis = pd.DataFrame()
        if API_type == "tmdb":
            df_apis = API_util.df_tmdb
        elif API_type == "spotify":
            df_apis = API_util.df_spotify

        # 获取task_plan中的主API,并进行去重
        task_plan = re.sub(r'^```json\s*|\s*```$', '', task_plan, flags=re.MULTILINE)
        task_plan = json.loads(task_plan)
        primary_APIs = set()
        for item in task_plan:
            primary_API = item.get("Primary API")
            if primary_API:
                primary_APIs.add(primary_API)

        API_documentation = ''''''
        for API_name in primary_APIs:
            for _, row in df_apis.iterrows():
                if row["endpoint_name"] == API_name:
                    APIs_temp = f'''

endpoint name: {row["endpoint_name"]}
description: {row["endpoint_description"]}
parameters: {row["parameters"]}
response_schema: {row["response_schema"]}'''
                    API_documentation += APIs_temp
        return API_documentation

if __name__ == '__main__':
    task_plan = '''[
  {
    "task": "Search for Sofia Coppola's person details",
    "Primary API": "GET /search/person",
    "Alternative APIs": ["GET /person/popular"]
  },
  {
    "task": "Retrieve Sofia Coppola's person ID",
    "Primary API": "GET /person/{person_id}",
    "Alternative APIs": []
  },
  {
    "task": "Retrieve Sofia Coppola's movie credits",
    "Primary API": "GET /person/{person_id}/movie_credits",
    "Alternative APIs": ["GET /credit/{credit_id}"]
  },
  {
    "task": "Count the number of movies directed by Sofia Coppola",
    "Primary API": "GET /person/{person_id}/movie_credits",
    "Alternative APIs": []
  }
]'''
    print(API_util.get_documentation_design(task_plan,"tmdb"))
    print("##################################")
    print(API_util.get_documentation_design_implementation(task_plan,"tmdb"))



