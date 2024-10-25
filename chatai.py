from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

from langchain_core.output_parsers import StrOutputParser
output_parser=StrOutputParser()

templete="""You are a helpful assistant
You have access to previous chats : {chat_history}
User ask:{text}"""

from langchain_core.prompts import ChatPromptTemplate
prompt= ChatPromptTemplate.from_template(templete)

chain=prompt | llm | output_parser

from langchain_core.messages import HumanMessage, AIMessage
chat_history=[]


while True:
    print("====================")
    print("=====================")
    user_ask=input(">>")
    if user_ask.lower()=='exit':
        break
    chat_history.append(HumanMessage(content=user_ask))
    response=chain.invoke({"text":user_ask,"chat_history": chat_history})
    chat_history.append(AIMessage(content=response))
    print(">>>",response)
