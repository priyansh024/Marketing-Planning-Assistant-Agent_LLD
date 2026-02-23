import streamlit as st
from marketing_planner_agent.agent import MarketingAgent

#  Page configuration
st.set_page_config(
    page_title="Marketing Planner Agent",
    page_icon="📈",
    layout="wide"
)

# --- NEW: Initialize session state for history ---
if "history" not in st.session_state:
    st.session_state.history = []
if "show_history" not in st.session_state:
    st.session_state.show_history = False


st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

/* Input box */
.stTextArea textarea {
    background-color: #1c1f26;
    color: white;
    border-radius: 10px;
    padding: 12px;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(90deg, #00C9A7, #00B4D8);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #00B4D8, #00C9A7);
}
</style>
""", unsafe_allow_html=True)

#  Sidebar
st.sidebar.title("🚀 Planner Agent")
st.sidebar.write("AI-powered marketing planning tool")
st.sidebar.write("---")
st.sidebar.write("Built with Streamlit")

# --- NEW: History UI in Sidebar ---
st.sidebar.write("### 📜 Session History")

col_h1, col_h2 = st.sidebar.columns(2)
with col_h1:
    if st.button("History"):
        st.session_state.show_history = not st.session_state.show_history
with col_h2:
    if st.button("Clear History"):
        st.session_state.history = []
        st.session_state.show_history = False
        st.rerun()

if st.session_state.show_history:
    if not st.session_state.history:
        st.sidebar.info("No plans generated yet.")
    else:
        # Show history in reverse order (newest first)
        for idx, (past_goal, past_plan) in enumerate(reversed(st.session_state.history)):
            with st.sidebar.expander(f"Goal: {past_goal[:25]}..."):
                st.write(past_plan[:150] + "...")
                # Download button for historical reports
                st.download_button(
                    label="📥 Download this report",
                    data=past_plan,
                    file_name=f"marketing_report_past_{idx}.txt",
                    mime="text/plain",
                    key=f"dl_hist_{idx}"
                )
st.sidebar.write("---")

#  Initialize agent
agent = MarketingAgent()

#  Header
st.markdown("<h1 style='text-align: center;'>📈 Marketing Planner Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9aa0a6;'>Generate AI-powered marketing strategies in seconds</p>", unsafe_allow_html=True)

st.write("")

#  Centered layout
col1, col2, col3 = st.columns([1,2,1])

with col2:
    goal = st.text_area(
        "Enter Marketing Goal",
        placeholder="Example: Create a marketing strategy for an online clothing store...",
        height=140
    )

    generate = st.button("Generate Plan")

#  Generate output
if generate:
    if goal.strip():

        with st.spinner("Creating your marketing strategy..."):
            raw_result = agent.run(goal)

        #  Extract actual text if returned as dict
        if isinstance(raw_result, dict) and "output" in raw_result:
            result = raw_result["output"]
        else:
            result = str(raw_result)

        #  Clean formatting artifacts
        result = result.replace("\\n", "\n")   # fix newline escapes
        result = result.replace("**", "")      # remove markdown bold
        result = result.replace("##", "")      # remove headings
        result = result.replace("|", "")       # remove table pipes
        result = result.replace("  ", " ")     # remove extra spaces
        result = result.replace("<br>", "\n")   #  remove HTML breaks
        result = result.replace("<br/>", "\n")

        # --- NEW: Save the successfully generated goal and result to history ---
        st.session_state.history.append((goal, result))

        st.success(" Plan Generated Successfully")

        # --- NEW: Download Button for the newly generated report ---
        st.download_button(
            label="📥 Download Marketing Report",
            data=result,
            file_name="marketing_strategy_report.txt",
            mime="text/plain"
        )

        st.markdown("### 📊 Strategy Output")

       
        st.markdown("""
        <div style="background-color:#1c1f26;
                    padding:25px;
                    border-radius:12px;
                    border:1px solid #2a2f3a;
                    line-height:1.7;
                    font-size:18px;">
        """, unsafe_allow_html=True)

        st.write(result)

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("⚠ Please enter a marketing goal")