import sys
import os

# Add the parent directory (RAGImplementation) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from retriever.retriever import Retriever

if __name__ == "__main__":
    retriever = Retriever(model_name="paraphrase-MiniLM-L6-v2")
    retriever.index_documents("/home/amit/Repositories/PythonStuffs/ArtificialIntelligence/RAGImplementation/data/corpus/nepal.pdf")
    print("Documents indexed successfully.")