import streamlit as st
from rag import ask_rag

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Your AI Assistant", layout="centered")

# ---- SIDEBAR ----
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    if st.button("🗑 Reset Conversation"):
        st.session_state.messages = []

    st.markdown("""
    ### 👤 About Me  
                
    I’m a **Data Scientist & AI Developer** passionate about building intelligent systems and solving real-world problems.  
    I enjoy working with **AI, machine learning, and modern tech** to create impactful solutions.
    """)

    st.markdown(
        "[🐙 GitHub](https://github.com/Mohammadbk93)",
        unsafe_allow_html=True
    )

    st.markdown(
        "[💼 LinkedIn](https://www.linkedin.com/in/mohammad-bagheri-9a3a7922a/)",
        unsafe_allow_html=True
    )

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>🤖 Your AI Assistant</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; color: gray;'>I help you get detailed information about PhD programs.</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---- INIT CHAT MEMORY ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- DISPLAY CHAT HISTORY ----
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---- CHAT INPUT ----
user_input = st.chat_input("Ask something about the PhD program...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = ask_rag(user_input)

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)