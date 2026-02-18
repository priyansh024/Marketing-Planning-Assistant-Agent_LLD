from langchain.tools import tool

@tool
def budget_tool(task_name: str, requested_amount: float) -> str:
    """Validates budget availability for a specific marketing task."""
    # Mock validation logic
    if requested_amount > 5000:
        return f"Budget for '{task_name}' REJECTED: Requested ${requested_amount} exceeds limit of $5000."
    return f"Budget for '{task_name}' APPROVED: ${requested_amount} allocated."
