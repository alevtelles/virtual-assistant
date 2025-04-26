from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os

def processar_documento(documento):
    caminho = documento.arquivo.path

    loader = TextLoader(caminho)
    documentos = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documentos)

    persist_directory = f'vetores/{documento.assistente.id}'
    os.makedirs(persist_directory, exist_ok=True)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=persist_directory)
    vectorstore.persist()
