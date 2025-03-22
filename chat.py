import streamlit as st

from dotenv import load_dotenv

from llm import get_ai_message

#디자인
st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

#1. 제목
st.title("🤖 소득세 챗봇")
#2. 설명
st.caption("소득세에 관련된 모든 것을 답해드립니다!")

load_dotenv()
#채팅 메시지를 저장할 공간 만들기
#session_state는 앱이 꺼질 때까지 정보를 저장하는 공간임
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

#사용자가 보낸 메시지를 다시 화면에 표시
for message in st.session_state.message_list:
    with st.chat_message(message['role']):
        st.write(message['content'])

#사용자가 입력한 메시지 받기
#:= -> 입력과 동시에 변수에 저장하는 연산자임
if user_question := st.chat_input(placeholder="소득세에 관련된 궁금한 내용들을 말씀해주세요"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({'role':'user', 'content':user_question})
    with st.spinner("답변을 준비하고 있습니다..."):      
        ai_message = get_ai_message(user_question)
        with st.chat_message("ai"):
            st.write(ai_message)
        st.session_state.message_list.append({'role':'ai', 'content':ai_message})
        