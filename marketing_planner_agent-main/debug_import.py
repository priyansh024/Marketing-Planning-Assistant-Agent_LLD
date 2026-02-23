import sys
import os
import traceback

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from marketing_planner_agent.agent import MarketingAgent
    print("Agent initialized successfully")
except ImportError as e:
    print(f"ImportError caught: {e}")
    traceback.print_exc()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()
