from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

model = ChatOpenAI()

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

# load chat history
with open('Langchain_prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

while True:

    user_input = input("You: ")

    if user_input == 'exit':
            break
    
    # create prompt
    prompt = chat_template.invoke({'chat_history':chat_history, 'query': user_input})
    result = model.invoke(prompt)

    chat_history.append(HumanMessage(content = user_input))
    chat_history.append(AIMessage(content = result.content))

    print("AI ", result.content)

print(chat_history)
