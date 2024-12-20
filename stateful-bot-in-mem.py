import os
import warnings
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_chroma import Chroma

warnings.filterwarnings("ignore")
load_dotenv()
chat_history = []

def chat_bot():
    loader = PyPDFLoader("data/LearningSpark2.0.pdf")
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))
    db = Chroma.from_documents(texts, embeddings)

    question = input("What is your question? ")
    vectorstore = db.as_retriever()

    chat = ChatOpenAI(verbose=True, temperature=0, model_name="gpt-3.5-turbo")

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, chain_type="stuff", retriever=vectorstore
    )

    while question != "quit":

        res = qa({"question": question, "chat_history": chat_history})
        history = (res["question"], res["answer"])
        chat_history.append(history)
        print("\n", res["answer"], "\n")
        question = input("Is there anything else? ")

if __name__ == "__main__":
    chat_bot()