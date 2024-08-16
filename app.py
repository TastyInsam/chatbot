#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import(
    HumanMessage,
    SystemMessage
)
import streamlit as st

chat_model = ChatOpenAI(model_name="gpt-3.5-turbo",temperature = 1)

st.title("<<오늘의 메뉴>>")
st.title("나다. \"_:blue[챗 램지]_\" :sunglasses:")
st.title("지금 기분이나 상황을 말해 봐!!!")
st.title("")

context = """
너는 사용자의 입맛 니즈를 잘 알고 있는 유명한 요리사야. 
고객이 음식 추천을 물으면 너는 고객의 요구에 맞추어 다양한 음식 중에서 한 가지 음식을 이유와 함께 추천해줘. 음식은 존재하는 것이고 요구사항에 정확히 들어맞아야 해.
답변은 반말로 시크하게 해. 응답 예시는 다음과 같아.
햄버거. 값이 싸고 간편하게 시킬 수 있으니까.
"""

content = st.text_input('인공지능 챗 램지가 당신의 식사를 추천합니다!!')

if st.button('추천받기'):
    with st.spinner("메뉴를 넘기는 중..."):
        message = [SystemMessage(content=context), HumanMessage(content=content)]

        result = chat_model.invoke(message).content
        st.write("오늘의 메뉴는...", result)
