from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.memory import ConversationSummaryMemory, FileChatMessageHistory
from dotenv import load_dotenv
import time

load_dotenv()

chat = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

memory = ConversationSummaryMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True,
    llm=chat,
)

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)
time.sleep(4)
chain = LLMChain(llm=chat, prompt=prompt, memory=memory, verbose=True)
while True:
    content = input(">> ")
    time.sleep(4.5)

    result = chain({"content": content})

    print(result["text"])
