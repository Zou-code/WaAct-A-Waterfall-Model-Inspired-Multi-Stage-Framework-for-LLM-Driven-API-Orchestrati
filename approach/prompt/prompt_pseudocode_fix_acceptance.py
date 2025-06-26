def prompt_pseudocode_fix_acceptance(requirement, requirement_gherkin, pseudocode, failure_reason, response, API_docs):
    prompt = '''\
You are an experienced software engineer tasked with revising a pseudocode implementation so that it correctly satisfies the user's original requirement and passes the acceptance test.

You are provided with:
- The original **user requirement** (natural language)
- Its **Gherkin representation** (Given-When-Then format)
- The current **pseudocode**, which was derived from the above
- The **reason the acceptance test failed**
- The **actual output** of the generated code
- A set of **API documentations** that can be used to implement the desired logic

---

## Your goal:

Revise the pseudocode to ensure that, once converted into executable code:
1. It fully implements the **user’s intent**.
2. It satisfies the behavior described in the **Gherkin acceptance criteria**.
3. It corrects the failure described in the test report.
4. It optionally replaces or reuses **appropriate APIs** as necessary.
5. It produces output matching expected structure and semantics.

---

User Requirement:
{user_requirement}

Gherkin Specification:
{requirement_gherkin}

Current Pseudocode:
{pseudocode}

Acceptance Test Failure Reason:
{failure_reason}

Actual Output of the Code:
{response}

API Documentation:
{API_docs}

Return only the **revised pseudocode**, rewritten to satisfy the requirement and pass the acceptance test.
Make minimal but necessary changes — preserve any parts that are still valid.
If needed, restructure the output logic or change which APIs are used.
Focus entirely on improving the **logic, sequence, and correctness** of the pseudocode.
'''
    prompt = prompt.replace("{user_requirement}", requirement).replace("{requirement_gherkin}", requirement_gherkin).replace(
        "{pseudocode}", pseudocode).replace("{failure_reason}", failure_reason).replace(
        "{response}", response).replace("{API_docs}", API_docs)

    return prompt


