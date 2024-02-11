from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings


load_dotenv()

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=100)


embeddings = OpenAIEmbeddings()

emb = embeddings.embed_query("Hello world")
print(emb)

loader = TextLoader(
    r"C:\Users\ishan\Downloads\ChatGPT and LangChain The Complete Developers Masterclass\Code New\facts\facts.txt"
)

docs = loader.load_and_split(
    text_splitter=text_splitter,
)

db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="emb")

results = db.similarity_search_with_score(
    "What is an interesting fact about the English Language?", k=2
)

for results in results:
    print("\n")
    print(results[1])
    print(results[0].page_content)
