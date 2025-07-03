# school:
# author:
# createTime: 2025/5/12 16:22
import pandas as pd

from requirement import RequirementAnalysis
from design import Design
from implementation import Implementation
from acceptance import Acceptance
from Debugging import Debugging
import re
import json
from util.API_documentation_util import API_util
import logging
import time

# 获取当前时间并格式化
current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

# 定义日志文件名
log_filename = f"../log/log_WaAct/{current_time}.log"

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志格式
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),  # 文件处理器
        logging.StreamHandler()  # 控制台处理器
    ]
)

class WaAct:
    def __init__(self, API_type):
        self.API_type = API_type

    def run(self, requirement):
        requirement_analysis = RequirementAnalysis()

        # Note 执行需求层，获取修改
        req, req_gherkin = requirement_analysis.requirement_run(requirement)
        logging.info("Original Requirement:\n" + req)
        logging.info("Gherkin Scenarios:\n"+req_gherkin)

        # Note 执行设计层，获取任务规划和伪代码
        design = Design()
        task_plan, pseudocode = design.design_run(req, req_gherkin)
        logging.info("Task Plan:\n" + task_plan)
        logging.info("Pseudocode:\n" + pseudocode)

        debugging = Debugging()

        ERROR = True
        IMPL_ERROR = False
        count = 0

        executable_code = ''

        while ERROR and count < 30:
            # 首次执行，或伪代码已被修改，需要根据伪代码生成可运行的代码
            impl = Implementation(self.API_type)
            if not IMPL_ERROR:
                # Note 执行实现层，获取可执行代码
                executable_code = impl.code_generation(task_plan, req, req_gherkin, pseudocode)
                logging.info("Executable Code:\n" + executable_code)
            result = impl.run_code(executable_code)
            if result.stdout:
	response = result.stdout
	logging.info(response)
                # Note 进行验收测试，判断是否通过
                acceptance = Acceptance()
                accept, reason = acceptance.accept_validation(req, req_gherkin, response)

                if accept is True:
                    logging.info("Acceptance Test Passed!")
                    return response
                else:
                    # Note 根据验收测试不通过的原因，修改伪代码
                    logging.warning("Acceptance Test Failed!")
                    API_doc = API_util.get_API_documentation_pseudocode_fix(task_plan, self.API_type)
                    pseudocode = debugging.pseudocode_fix_acceptance(req, req_gherkin, pseudocode, reason, response, API_doc)
                    logging.info("Fixed Pseudocode in the Acceptance Test:\n" + pseudocode)
                    count += 1
                    continue

            if result.stderr:
                error_message = result.stderr
                logging.error(result.stderr)
                # Note 进行错误分析，判断错误是设计层还是实现层
                API_doc = API_util.get_API_documentation_pseudocode_fix(task_plan, self.API_type)
                error_report = json.loads(debugging.error_analysis(req,req_gherkin, pseudocode,executable_code,error_message, API_doc))
                logging.info("error_report:\n" + error_report)
                error_aspect = error_report.get("error_aspect")
                error_description = error_report.get("error_description")
                if error_aspect == "Design":
                    # Note 错误判断为设计层，对设计阶段的伪代码进行修复
                    pseudocode = debugging.pseudocode_fix_debugging(req, req_gherkin, pseudocode, executable_code, error_message, error_description, API_doc)
                    logging.info("Fixed Pseudocode in the Implementation:\n" + pseudocode)
                    count += 1
                    continue
                if error_aspect == "Implementation":
                    # Note 错误判断为实现层，对实现层的可执行代码进行修复
                    API_doc_impl = API_util.get_documentation_implementation(task_plan, self.API_type)
                    executable_code = debugging.code_fix(req, req_gherkin, pseudocode, executable_code, error_message, error_description, API_doc)
                    logging.info("Fixed Executable Code in the Implementation:\n" + executable_code)
                    IMPL_ERROR = True
                    count += 1
                    continue
        if count == 30:
            return "Failed"


if __name__ == '__main__':

    des_dd = WaAct('tmdb')
    requirement = "Give me the number of movies directed by Sofia Coppola."
    result = des_dd.run(requirement)
    print(result)



