# 기본 버튼 입력 예제
# 상태변화 session
import streamlit as st
# session 처리
if st.session_state:
    cnt_session = st.session_state['cnt']
    cnt_session += 1
    st.session_state['cnt'] = cnt_session
    print("기본 버튼 입력 예제: cnt=",cnt_session)
else: 
    st.session_state['cnt'] = 1
    cnt_session = st.session_state['cnt'] # cnt가 0일떄도 출력.
# cnt 변수값 else에서 1로 정의가 되면 if에서 1+1 =2 가 cnt_session이 되고 
# 실행 될 떄 마다 1씩 증가하여 출력됨.    

st.title("스트림릿의 버튼 입력 사용 예")
st.text("버튼 클릭 회수: {0}".format(cnt_session)) 
# st.header("버튼 클릭 회수: {0}".format(cnt_session)) title 크기로 바꾸어줌
clicked = st.button('버튼 1')
st.write('버튼 1 클릭 상태:', clicked)

if clicked:
     st.write('버튼 1을 클릭했습니다.' )
else:
     st.write('버튼 1을 클릭하지 않았습니다.' )
        
clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태:', clicked)

if clicked:
     st.write('버튼 2를 클릭했습니다.' )
else:
     st.write('버튼 2를 클릭하지 않았습니다.' )
