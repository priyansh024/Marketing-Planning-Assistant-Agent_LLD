# 📈 Marketing Planner Agent

An AI-powered, autonomous agent that plans and schedules complex marketing tasks. Built with **Streamlit**, **LangChain**, and **Google Gemini**, this tool breaks down high-level marketing goals into actionable, structured strategies.

## ✨ Features
* **Interactive Web UI:** Clean, user-friendly interface powered by Streamlit.
* **Goal Decomposition:** Automatically breaks high-level goals into structured sub-tasks (Target audience, Channels, Keywords, Budget, Timeline).
* **Mock Tool Integration:** Simulates real-world validation using custom LangChain tools (Ad Library, Keyword Research, Budget Validator, Scheduler).
* **Session History:** Keeps track of your previously generated plans during your session.
* **Export Reports:** Instantly download your generated marketing strategies as text files.
* **CLI Support:** Run the agent directly from the terminal if preferred.

## 📁 Project Structure
```text
marketing_planner_agent/
# 📈 Marketing Planner Agent

An AI-powered, autonomous agent that plans and schedules complex marketing tasks. Built with **Streamlit**, **LangChain**, and **Google Gemini**, this tool breaks down high-level marketing goals into actionable, structured strategies.

## ✨ Features
* **Interactive Web UI:** Clean, user-friendly interface powered by Streamlit.
* **Goal Decomposition:** Automatically breaks high-level goals into structured sub-tasks.
* **Mock Tool Integration:** Simulates real-world validation using custom tools (Ad Library, Keyword Research, Budget Validator, Scheduler).
* **Session History:** Keeps track of your previously generated plans.
* **Export Reports:** Download generated marketing strategies as text files.

## 📁 Project Structure
```text
marketing_planner_agent/
├── marketing_planner_agent/    # Main package folder
│   ├── tools/ |-                # Mock tool implementations
│   ├── .env                    # Environment variables (ignored in git)
│   ├── agent.py                # LangChain agent orchestration
│   ├── config.py               # Configuration management
│   ├── main.py                 # CLI entry point
│   ├── planner.py              # Data models and formatting
│   ├── README.md               # Project documentation
│   └── requirements.txt        # Project dependencies
├── app.py                      # Streamlit web interface (Main UI)
├── debug_import.py             # Debugging script
└── debug_output.txt            # Debugging logs (ignored in git)

step - 1
# Install all dependencies
pip install -r requirements.txt

step - 2
# add your api-key on .env file
GOOGLE_API_KEY=your_google_api_key_here
not exists create first then add

step - 3 

#run streamlit command for run 
python -m streamlit run app.py