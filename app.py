import streamlit as st

if "conversation_stage" not in st.session_state:
    st.session_state.conversation_stage = "init"
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="Hotel Booking AI Agent")
st.title("🛎️ AI Hotel Booking Assistant")

from llm_agent.llm_agent import agent_executor

st.subheader("💬 Gemini Chat Agent")

user_input = st.chat_input("Tulis pesan...")

if user_input:
    with st.spinner("Sedang berpikir..."):
        response = agent_executor.run(user_input)
        st.chat_message("🧍").write(user_input)
        st.chat_message("🤖").write(response)

