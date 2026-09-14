from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI() #model='gpt-5-nano' 'gpt-4', #gpt-5.6-luna'

st.header('Reasearch Tool')

# user_input = st.text_input("Enter your ptompt")
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('Langchain_prompts/template.json')

prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input': length_input
})

if st.button("summarize"):

    with st.spinner("Generating summary..."):
        result = model.invoke(prompt)

    st.success("Summary generated!")
    st.write(result.content)    