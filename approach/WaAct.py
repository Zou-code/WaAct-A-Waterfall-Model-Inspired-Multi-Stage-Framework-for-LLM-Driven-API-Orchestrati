
import pandas as pd

from requirement import RequirementAnalysis
from design import Design
from implementation import Implementation
from acceptance import Acceptance
import re
import json
from util.API_documentation_util import API_util

# TODO 添加log部分的代码

class WaAct:
    def __init__(self):
        pass

    def run(self, requirement):
        requirement_analysis = RequirementAnalysis()

        # Note 执行需求层，获取修改
        req, req_gherkin = requirement_analysis.requirement_run(requirement)
        print(req)
        print(req_gherkin)


        ERROR = True
        FIRST_RUN = True

        while ERROR:
            if FIRST_RUN:
                # Note 执行设计层，获取任务规划和伪代码
                design = Design()
                task_plan, pseudocode = design.design_run(req, req_gherkin)
                print(task_plan)
                print(pseudocode)

                # Note 执行实现层，获取可执行代码
                impl = Implementation('tmdb')
                executable_code = impl.code_generation(task_plan, req, req_gherkin, pseudocode)
                print(executable_code)
                result = impl.run_code(executable_code)
                print(result)
                if result.stdout:
                    acceptance = Acceptance()
                    accept = acceptance.accept_validation(req, req_gherkin, result)

                    if accept == 'true':
                        return result
                    else:
                        pass
                    pass

                if result.stderr:
                    error_message = result.stderr
                    print(result.stderr)
                    pass



if __name__ == '__main__':

    des_dd = WaAct()
    requirement = "Give me the number of movies directed by Sofia Coppola."
    result = des_dd.run(requirement)
#
#     # requirement_gherkin = des_dd.run(requirement)
#     # print(requirement_gherkin)
#
#     requirement_gherkin = '''\
# ```gherkin
# Feature: Retrieve movie count by director
#
#   Scenario: Get number of movies directed by Sofia Coppola
#     Given a database of movies and directors
#     When I request the count of movies directed by "Sofia Coppola"
#     Then I should receive the correct number of movies
# ```'''
#
#     task_plan = '''```json
# [
#   {
#     "task": "Search for Sofia Coppola's person details",
#     "Primary API": "GET /search/person",
#     "Alternative APIs": ["GET /person/popular"]
#   },
#   {
#     "task": "Retrieve Sofia Coppola's person ID",
#     "Primary API": "GET /person/{person_id}",
#     "Alternative APIs": []
#   },
#   {
#     "task": "Retrieve Sofia Coppola's movie credits",
#     "Primary API": "GET /person/{person_id}/movie_credits",
#     "Alternative APIs": ["GET /credit/{credit_id}"]
#   },
#   {
#     "task": "Count the number of movies directed by Sofia Coppola",
#     "Primary API": "GET /person/{person_id}/movie_credits",
#     "Alternative APIs": []
#   }
# ]
# ```
# '''
#
#     pseudocode = '''```pseudocode
# FUNCTION get_movie_count_by_director(director_name):
#     // Step 1: Search for the director by name to get their ID
#     search_results = CALL_API GET /search/person WITH PARAMS {
#         query: director_name
#     }
#
#     // Step 2: Find the correct person in search results (filter by known_for_department if available)
#     director_id = NULL
#     FOR EACH person IN search_results.results:
#         IF person.known_for_department == "Directing" AND person.name == director_name:
#             director_id = person.id
#             BREAK
#
#     IF director_id IS NULL:
#         RETURN ERROR "Director not found"
#
#     // Step 3: Get all movie credits for the director
#     movie_credits = CALL_API GET /person/{director_id}/movie_credits
#
#     // Step 4: Filter and count only directing credits
#     movie_count = 0
#     FOR EACH movie IN movie_credits.crew:
#         IF movie.job == "Director":
#             movie_count = movie_count + 1
#
#     RETURN movie_count
#
# // Main execution
# movie_count = get_movie_count_by_director("Sofia Coppola")
# OUTPUT movie_count
# ```'''
#     design = Design()
#     # # plan = design.task_plan(requirement,requirement_gherkin)
#     # # print(plan)
#     #
#     pseudocode = design.pseudocode_generation(requirement, requirement_gherkin, task_plan)
#     print(pseudocode)
#
#     # API_documentation = des_dd.get_API_documentation_implementation(task_plan)
#     API_documentation = API_util.get_documentation_implementation(task_plan, "tmdb")
#     print(API_documentation)
#
#     #
#     Implementation = Implementation('tmdb')
#     executable_code = Implementation.code_generation(requirement, API_documentation, pseudocode, "tmdb")
#     print(executable_code)
#     # print(pseudocode)
#     executable_code = Implementation.code_generation(requirement, API_documentation, pseudocode, "tmdb")
#     print(executable_code)
#     # print(pseudocode)


