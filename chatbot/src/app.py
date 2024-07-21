import streamlit as st
from src.utils import call_llama


st.title(":zap: Llama ChatBot")

# prompt = st.chat_input('Say something')
# if prompt:
#     st.chat_message('user').write(f"user has sent the following prompt:{prompt}")
st.caption("A Streamlit chatbot powered by:llama: Llama")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content":"How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    prompt += """
Make the response as short as possible, less than 1 paragraph. 
"""
    with st.spinner('Generating response...'):
        msg = call_llama('llama2', prompt)['response']
    st.session_state.messages.append({"role":"assistant", "content":msg})
    st.chat_message("assistant").write(msg)
