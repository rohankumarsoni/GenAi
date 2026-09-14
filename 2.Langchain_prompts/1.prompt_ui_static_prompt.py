from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI() #model='gpt-5-nano' 'gpt-4', #gpt-5.6-luna'

st.header('Reasearch Tool')

user_input = st.text_input("Enter your ptompt")

if st.button("summarize"):

    with st.spinner("Generating summary..."):
        result = model.invoke(user_input)

    st.success("Summary generated!")
    st.write(result.content)


## Here user can pass any paper name that hs not ben published 
## LLM can haulcinate, we can ue dynamic prompt to solve this problem 