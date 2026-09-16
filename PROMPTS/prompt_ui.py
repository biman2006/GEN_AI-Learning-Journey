from langchain_groq import ChatGroq

from dotenv import load_dotenv

import streamlit as st

from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model=ChatGroq( model="openai/gpt-oss-120b",
    temperature=0)

st.header("RESEARCH TOOL")

paper_input=st.selectbox("Select research paper Name", ["Select...", "Attention Is All You Need", "BERT : pre-training of Deep Bidirectional Transformers", "GPT-3:Language Models are Few-shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])


style_input=st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical Code-Oriented", "Mathematical"])

length_input=st.selectbox("select Explanation Length", ["Shot (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# Template

template =load_prompt("template.json")


if st.button("Summarize"):
        chain=template|model

        result=chain.invoke({'paper_input':paper_input,
                     'style_input':style_input,
                     'length_input':length_input})

        st.write(result.content)

    