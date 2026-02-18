from typing import List
from langchain.tools import tool

@tool
def keyword_tool(topic: str) -> List[str]:
    """Performs mock keyword research for a given topic."""
    # Mock data
    keywords = [
        f"{topic} best practices",
        f"how to start {topic}",
        f"{topic} software",
        f"top {topic} trends"
    ]
    return keywords
