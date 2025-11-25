# makktalan ai — Streamlit Chatbot

This project is a custom AI chatbot built using **Streamlit** and the **OpenAI API**.  
The interface provides a smooth, chat-style experience similar to modern AI assistants, with options to configure creativity, personality, and token limits.  
The assistant’s name in the app is **makktalan ai**.

---

## Features

### **• Interactive Chat UI**
A clean conversational interface powered by `st.chat_message` and `st.chat_input`.

### **• Custom AI Personality**
You can define how makktalan ai behaves via a system prompt located in the sidebar.

### **• Adjustable Model Behavior**
Control:
- Temperature (creativity)
- Maximum response length (token limit)
- System instructions

### **• Chat History Memory**
Conversation is stored using `st.session_state`, allowing the AI to maintain context over multiple messages.

### **• Reset Conversation**
A single button clears the active chat and refreshes the assistant.

### **• Fully Customizable Bot Name**
The bot uses a variable called `BOT_NAME`, making it easy to rename or theme the chatbot.

---

## File Structure

