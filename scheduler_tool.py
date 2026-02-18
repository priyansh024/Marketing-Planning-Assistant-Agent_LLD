from typing import List
from langchain.tools import tool

@tool
def scheduler_tool(tasks: List[str]) -> str:
    """Creates a mock execution timeline for a list of tasks."""
    timeline = "Execution Schedule:\n"
    for i, task in enumerate(tasks):
        timeline += f"Day {i+1}: {task}\n"
    return timeline
