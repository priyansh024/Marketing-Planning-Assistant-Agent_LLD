# Marketing Planning Assistant Agent

An autonomous agent that plans and schedules complex marketing tasks using LangChain and mock tools.

## Features
- **Goal Decomposition**: Breaks high-level goals into structured sub-tasks.
- **Resource Validation**: Uses mock tools to check budget, keywords, and ad libraries.
- **Dependency Management**: Determines the correct execution order.
- **Optimized Scheduling**: Generates a timeline for task execution.

## Project Structure
```
marketing_planner_agent/
│
├── main.py             # CLI entry point
├── agent.py            # Agent orchestration logic
├── planner.py          # Data models and formatting
├── tools/              # Mock tool implementations
│   ├── ad_library_tool.py
│   ├── keyword_tool.py
│   ├── budget_tool.py
│   └── scheduler_tool.py
├── config.py           # Configuration management
├── requirements.txt    # Dependencies
└── .env.example        # Environment variable template
```

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your `OPENAI_API_KEY`.
4. Run the agent:
   ```bash
   python main.py "Competitor Ads Analysis"
   ```
