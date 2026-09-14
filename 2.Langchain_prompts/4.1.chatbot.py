from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

model = ChatOpenAI()

chat_history = []

while True:

    user_input = input("You: ")

    if user_input =='exit':
        break

    result = model.invoke(user_input)
    print("AI : ", result.content)

   ## here the cahtbot dont have any memory 
   # we need to save the conversation in a list  
