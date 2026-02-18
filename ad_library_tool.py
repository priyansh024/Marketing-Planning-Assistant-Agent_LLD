from typing import List
from langchain.tools import tool

@tool
def ad_library_tool(competitor_name: str) -> List[str]:
    """Fetches mock competitor ad data from the ad library."""
    # Mock data
    ads = [
        f"Buy {competitor_name}'s new product! 20% off!",
        f"{competitor_name} - Number 1 in the market.",
        f"Limited time offer from {competitor_name}."
    ]
    return ads
