import streamlit as st
import datetime
from vector_store import create_vector_store
from prompt_engine import build_advanced_prompt
from generator import generate_content

st.set_page_config(page_title="GenAI Marketing Tool", page_icon="🚀", layout="wide")

# FIXED CSS (text color added)
st.markdown("""
<style>
.big-title {font-size:40px; font-weight:bold; color:#4CAF50;}
.card {
    background-color:#ffffff;
    color:#000000;
    padding:20px;
    border-radius:10px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🚀 Marketing Content Generator</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    product = st.text_input("📦 Product Name")
    audience = st.text_input("🎯 Target Audience")

with col2:
    tone = st.selectbox("🎨 Tone", ["Professional", "Casual", "Motivational", "Friendly", "Premium"])
    format_type = st.selectbox("📝 Content Type", ["Ad Copy", "Instagram Post", "Email Marketing"])

# History storage
if "history" not in st.session_state:
    st.session_state.history = []

# Toggle history button
show_history = st.toggle("📜 Show History")

# Generate
if st.button("✨ Generate Content"):
    if not product or not audience:
        st.warning("⚠️ Please fill all fields")
    else:
        with st.spinner("Generating..."):
            vector_db = create_vector_store()

            query = f"{product} {audience} {tone}"
            docs = vector_db.similarity_search(query, k=2)

            context = "\n".join([doc.page_content for doc in docs])

            prompt = build_advanced_prompt(product, audience, tone, context, format_type)

            result = generate_content(prompt)

            st.session_state.history.append({
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "product": product,
                "output": result
            })

            st.markdown("### 📢 Generated Content")
            st.markdown(f'<div class="card">{result}</div>', unsafe_allow_html=True)

# Show history ONLY if toggle ON
if show_history and st.session_state.history:
    st.markdown("### 🕘 Previous Outputs")

    for item in reversed(st.session_state.history):
        st.markdown(f"""
        <div class="card">
        <b>⏰ {item['time']}</b><br>
        <b>📦 {item['product']}</b><br><br>
        {item['output']}
        </div>
        """, unsafe_allow_html=True)