import streamlit as st

st.set_page_config(page_title="Chatbot Demo", page_icon="💬", layout="centered")

st.title("🤖 Chatbot Demo")
st.markdown("This is a front-end mockup for a chatbot. No backend or model connected.")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("증상을 입력하세요.")

# If user submits a message
if user_input:
    # Save user message
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    
    # Placeholder response from bot
    bot_response = f"You said: **{user_input}** (this is a mock reply)"
    st.session_state.chat_history.append({"role": "bot", "message": bot_response})

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.write(chat["message"])
    else:
        with st.chat_message("assistant"):
            st.write(chat["message"])
