from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from redundant_filter_retriever import RedundantFilterRetriever
from langchain.chat_models import ChatOpenAI

load_dotenv()

embeddings = OpenAIEmbeddings()

chat = ChatOpenAI()

db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings,
)

retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db,
)

chain = RetrievalQA.from_chain_type(llm=chat, retriever=retriever, chain_type="stuff")

result = chain.run("What is an interesting fact about the English Language?")

print(result)
