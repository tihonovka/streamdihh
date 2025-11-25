import streamlit as st
from openai import OpenAI

API_KEY = "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"

client = OpenAI(api_key=API_KEY)

# A BOT NEVE
BOT_NAME = "makktalan ai"

st.set_page_config(page_title=BOT_NAME, page_icon="🤖", layout="centered")

# ---- SIDEBAR ----
with st.sidebar:
    st.title(f"🤖 {BOT_NAME} Settings")
    st.markdown("Configure how the AI behaves.")

    system_prompt = st.text_area(
        "System prompt (AI personality)",
        value=f"You are {BOT_NAME}, a concise helpful assistant.",
        height=120,
    )

    temperature = st.slider(
        "Creativity (temperature)",
        min_value=0.0,
        max_value=1.5,
        value=0.7,
        step=0.1,
    )

    max_tokens = st.slider(
        "Max response tokens",
        min_value=50,
        max_value=1000,
        value=400,
        step=50,
    )

# FŐCÍM
st.title(f"🤖 Chat with {BOT_NAME}")

# ---- SESSION STATE ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": f"You are {BOT_NAME}, a helpful assistant."}
    ]

# Chat előzmények kirajzolása
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# ---- INPUT ----
user_input = st.chat_input("Type your message here...")


def ask_model(messages, temperature=0.7, max_tokens=400):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


# ---- HANDLE INPUT ----
if user_input:
    st.session_state.messages = [
        m for m in st.session_state.messages if m["role"] != "system"
    ]
    st.session_state.messages.insert(0, {"role": "system", "content": system_prompt})

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_reply = ask_model(
                st.session_state.messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            st.markdown(ai_reply)

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# ---- CLEAR BUTTON ----
st.divider()
if st.button("Clear conversation"):
    st.session_state.messages = [
        {"role": "system", "content": f"You are {BOT_NAME}, a helpful assistant."}
    ]
    st.rerun()
 