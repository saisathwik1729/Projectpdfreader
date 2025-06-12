import fitz  # PyMuPDF
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def process_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def answer_question(file_path, question):
    loader = SimpleDirectoryReader(input_files=[file_path])
    documents = loader.load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    return query_engine.query(question).response