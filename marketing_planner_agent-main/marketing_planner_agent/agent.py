from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from marketing_planner_agent.config import GOOGLE_API_KEY, MODEL_NAME
from marketing_planner_agent.tools.ad_library_tool import ad_library_tool
from marketing_planner_agent.tools.keyword_tool import keyword_tool
from marketing_planner_agent.tools.budget_tool import budget_tool
from marketing_planner_agent.tools.scheduler_tool import scheduler_tool


class MarketingAgent:
    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")

        # Gemini LLM
        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            temperature=0.3,
            google_api_key=GOOGLE_API_KEY
        )

        # Register tools
        self.tools = {
            "ad_library_tool": ad_library_tool,
            "keyword_tool": keyword_tool,
            "budget_tool": budget_tool,
            "scheduler_tool": scheduler_tool
        }

    # ==================================================
    # Main function called from Streamlit
    # ==================================================
    def run(self, goal: str):

        # -------- Step 1: Ask LLM to create strategy ----------
        prompt = f"""
Decompose the following marketing goal into a complete actionable marketing plan.

Include:
1. Target audience
2. Channels
3. Keywords
4. Budget estimate
5. Timeline
6. Step-by-step tasks

Goal:
{goal}
"""

        messages = [
            SystemMessage(content="You are an expert Marketing Planning Assistant."),
            HumanMessage(content=prompt)
        ]

        response = self.llm.invoke(messages)

        # -------- Step 2: Simulate tool usage (safe defaults) ----------
        try:
            keywords = self.tools["keyword_tool"].invoke(goal)
        except:
            keywords = "Keyword suggestions unavailable"

        try:
            budget = self.tools["budget_tool"].invoke({
                "task_name": "Marketing Campaign",
                "requested_amount": 5000
            })
        except:
            budget = "Budget estimate unavailable"

        try:
            schedule = self.tools["scheduler_tool"].invoke("4 week campaign")
        except:
            schedule = "Schedule unavailable"

        # -------- Step 3: Combine everything ----------
        resource_output = f"""

--- Tool Insights ---
Keywords: {keywords}
Budget Plan: {budget}
Schedule: {schedule}
"""

        final_output = f"{response.content}\n{resource_output}"

        return {"output": final_output}