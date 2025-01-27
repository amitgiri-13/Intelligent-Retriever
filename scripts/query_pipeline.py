import sys
import os

# Add the parent directory (RAGImplementation) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pipeline.rag_pipeline import RAGPipeline

if __name__ == "__main__":
    pipeline = RAGPipeline("paraphrase-MiniLM-L6-v2","gpt2")
    query = "What is the main topic of the document? "
    response = pipeline.run(query, "/home/amit/Repositories/PythonStuffs/ArtificialIntelligence/RAGImplementation/data/corpus/nepal.pdf")
    print(response)