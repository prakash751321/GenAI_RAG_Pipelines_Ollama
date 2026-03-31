from langchain_community.document_loaders import TextLoader, WebBaseLoader, PyPDFLoader
from bs4.filter import SoupStrainer

#   DATA INGESTION PHASE

# DATA LOADING

#   Reading the Speech.txt file using TextLoader

# loader=TextLoader("speech.txt")

# doc=loader.load()
# print(doc)                        

# /////////////////////////////////////////////////

#   Reading the web page details using WebBaseLoader

# loader=WebBaseLoader(web_paths=["https://git-scm.com/"],
#                      bs_kwargs=dict(parse_only=SoupStrainer(
#                          class_=("inner", "masthead")

#                      ))
#                      )
# text_doc=loader.load()
# print(text_doc)

# //////////////////////////////////////////////

#   Reading from a PDF file

loader=PyPDFLoader("Notes_on_AI.pdf") 
pdf_load=loader.load()
print(pdf_load)



