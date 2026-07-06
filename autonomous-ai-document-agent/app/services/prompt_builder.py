"""
Prompt Builder Service.

Builds well-structured prompts for different autonomous agent tasks.
"""

from typing import List


class PromptBuilder:
    """
    Builds prompts for every LangGraph node.
    """

    @staticmethod
    def build_planner_prompt(request: str) -> str:
        """
        Prompt for the Planner Node.
        """

        return f"""
You are an Autonomous AI Planning Agent.

Your responsibility is to understand the user's request and generate
a logical execution plan.

User Request:
{request}

Instructions:

1. Understand the user's objective.
2. Break the task into sequential steps.
3. Return only a numbered execution plan.
4. Keep the plan concise.
"""

    @staticmethod
    def build_decision_prompt(
        request: str,
        execution_plan: List[str],
    ) -> str:
        """
        Prompt for the Decision Node.
        """

        plan = "\n".join(execution_plan)

        return f"""
You are an AI Decision Agent.

User Request:
{request}

Execution Plan:
{plan}

Determine:

1. Best document type.
2. Missing information.
3. Reasonable assumptions.

Return your answer clearly.
"""

    @staticmethod
    def build_executor_prompt(
        request: str,
        document_type: str,
        assumptions: List[str],
    ) -> str:
        """
        Prompt for the Executor Node.
        """

        assumption_text = "\n".join(assumptions)

        return f"""
You are an AI Document Generator.

Generate a professional {document_type}.

User Request:
{request}

Assumptions:
{assumption_text}

Requirements:

- Professional language
- Proper headings
- Business format
- Detailed content
"""

    @staticmethod
    def build_reflection_prompt(
        document: str,
    ) -> str:
        """
        Prompt for the Reflection Node.
        """

        return f"""
You are an AI Quality Reviewer.

Review the following document.

Document:

{document}

Check:

- Completeness
- Structure
- Grammar
- Professional tone
- Missing sections

If everything is correct,
reply with APPROVED.

Otherwise explain improvements.
"""