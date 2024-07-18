import json
import streamlit as st
with open('evaluation_criteria.json', 'r', encoding='utf8') as file:
    evaluation_criteria = json.load(file)
def evaluate_intro(client, GPT_MODEL, user_input):
    intro_standard = evaluation_criteria['intro']['standard']
    messages = [
        {"role": "system", "content": "너는 주니어 개발자의 입사지원서류의 완성도를 높여주는 컨설턴트 로봇이야. 주어진 기준에 맞춰서 분석하고 피드백과 개선(평가 기준을 반영한) 예시를 제공해서 json 형태로 응답"},
        {"role": "assistant", "content": f"다음과 같은 평가 기준으로 피드백을 진행할 것. {intro_standard}\n응답결과는 check(list of string), example(list of string)으로 리턴"},
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model=GPT_MODEL,
        response_format={"type": "json_object"},
        messages=messages,
        temperature=0.5
    )
    content_data = json.loads(response.choices[0].message.content)
    return content_data


def evaluate_skill_stack(client, GPT_MODEL, company_skills, user_input):
    company_skills =company_skills
    skillstack_standard = evaluation_criteria['skill_stack']['standard']
    messages = [
        {"role": "system", "content": "너는 주니어 개발자의 입사지원서류의 완성도를 높여주는 컨설턴트 로봇이야. 주어진 기준에 맞춰서 분석하고 피드백과 개선(평가 기준을 반영한) 예시를 제공해서 json 형태로 응답"},
        {"role": "assistant", "content": f"기술 스택에 항목에 대한 작성 내용을 다음과 같은 평가 기준으로 피드백을 진행할 것. 익히지 않은 기술 스택이 있을 수 있기 때문에 빠진 내용이 있다면 언급만 해주기. 예시사항은 기술 스택 항목만 작성하는게 원칙임. 기업 요구 사항 : {company_skills} \n평가정보 : {skillstack_standard}\n 응답결과는 check(list of string), example(list of string)으로 리턴"},
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
                model=GPT_MODEL,
                response_format={"type": "json_object"},
                messages=messages,
                temperature=0.5
            )
    content_data = json.loads(response.choices[0].message.content)
    return content_data

def evaluate_project_experience(client, GPT_MODEL, user_input):
    project_standard =evaluation_criteria['project']['standard'] 
    messages = [
        {"role": "system", "content": "너는 주니어 개발자의 입사지원서류의 완성도를 높여주는 컨설턴트 로봇이야. 주어진 기준에 맞춰서 분석하고 피드백과 개선(평가 기준을 반영한) 예시를 제공해서 json 형태로 응답"},
        {"role": "assistant", "content": f"프로젝트 경험 항목에 대한 작성 내용을 다음과 같은 평가 기준으로 피드백을 진행할 것. 예시사항은 기술 스택 항목만 작성하는게 원칙임. 평가정보 : {project_standard}\n응답결과는 check(list of string), example(list of string)으로 리턴"},
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model=GPT_MODEL,
        response_format={"type": "json_object"},
        messages=messages,
        temperature=0.5
    )
    content_data = json.loads(response.choices[0].message.content)
    return content_data

def display_evaluation_results(evaluation):
    if 'check' in evaluation:
        st.write("평가 체크리스트:")
        for content in evaluation['check']:
            st.success(content, icon="✅")
    if 'example' in evaluation:
        st.write("개선 예시:")
        for content in evaluation['example']:
            st.warning(content)