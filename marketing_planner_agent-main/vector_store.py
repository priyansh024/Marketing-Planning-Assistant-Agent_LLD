from langchain_community.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_store():
    with open("data/marketing_samples.txt", "r") as f:
        texts = f.readlines()

    embeddings = HuggingFaceEmbeddings()
    vector_db = FAISS.from_texts(texts, embeddings)
    return vector_db
