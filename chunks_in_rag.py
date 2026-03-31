from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma, FAISS, LanceDB
from langchain_ollama import OllamaEmbeddings


#   Data Ingestion layer

# loading the pdf
loader=PyPDFLoader("Notes_on_AI.pdf") 
pdf_load=loader.load()
# print(pdf_load)

# Converting to chunks

# splitting the texts into chunks, which are easy to store vector dbs
text_splitter=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ".", " ",""],chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(pdf_load)
# print(documents[:5])

# instead of creating obj again & again of ollamaembeddings calling once & stored in a variable & reuse it
embeddings=OllamaEmbeddings(model="llama3.1")

# Embeddings Layer

# Convert the chunks into vector embeddings & storing it in vector Db
db=Chroma.from_documents(
    documents[:20], 
    embedding=embeddings)


# Vector Database Queries
query="Definition of AI"
result=db.similarity_search(query)
print(result[0].page_content)


# FAISS Vector Databse

# f_db=FAISS.from_documents(documents[:20], embedding=embeddings)
# query="Definition of AI"
# result=f_db.similarity_search(query)
# print(result[0].page_content)



# With LanceDb

# l_db=LanceDB.from_documents(documents[:20], embedding=embeddings)
# query="Definition of AI"
# result=l_db.similarity_search(query)
# print(result[0].page_content)