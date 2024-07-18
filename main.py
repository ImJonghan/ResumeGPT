import streamlit as st
import os
from openai import OpenAI
import json
from evaluations import evaluate_intro, evaluate_skill_stack, display_evaluation_results, evaluate_project_experience
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(layout="wide")

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_MODEL = "gpt-4-turbo"
client = OpenAI(api_key=OPENAI_API_KEY)

with st.sidebar:
    st.header("😎멋사 파이썬 백엔드 스쿨 9기")
    st.divider()
    st.write("포트폴리오 작성 참고 내용")
    st.write("https://carbonated-cover-25d.notion.site/ee54c51838834e85b30d143abead4d77?pvs=4")  

st.info("포트폴리오를 점검해 봅시다!")
st.caption("같은 내용이어도 실행할 때마다 다른 결과가 나옵니다. 여러가지 관점으로 검토하고 자신에게 맞는 내용을 찾고 반영하면 좋겠습니다.")
tab1, tab2, tab3 = st.tabs(["🎙️인트로 점검", "🖥️기술 스택 점검", "🤝프로젝트 점검"])


with tab1:
    with st.form("intro_form"):
        user_input = st.text_area("Intro 내용 입력", placeholder="여기에 Intro 내용을 입력해주세요.", height=200)
        st.write()
        submit_button = st.form_submit_button("제출", use_container_width=True)
        if submit_button:
            intro_evaluation = evaluate_intro(client=client, GPT_MODEL=GPT_MODEL, user_input=user_input)
            display_evaluation_results(intro_evaluation)
with tab2:
    with st.form("skill_form"):
        company_info = st.text_area("대상 기업 요구 기술 스택",placeholder="대상 기업의 요구 정보를 넣어주세요")
        user_input = st.text_area("기술 스택 점검", placeholder="기술 스택 작성 내용을 입력해 주세요.")
        st.write()
        submit_button = st.form_submit_button("제출", use_container_width=True)
        if submit_button:
            skill_evaluation = evaluate_skill_stack(client, GPT_MODEL, company_info, user_input)
            display_evaluation_results(skill_evaluation)
with tab3:
    with st.form("project_form"):
        user_input = st.text_area("프로젝트 내용 점검", placeholder="하나의 프로젝트 내용만 넣어주세요", height=200)
        st.write()
        submit_button = st.form_submit_button("제출", use_container_width=True)
        if submit_button:
            project_evaluation = evaluate_project_experience(client, GPT_MODEL, user_input)
            display_evaluation_results(project_evaluation)
