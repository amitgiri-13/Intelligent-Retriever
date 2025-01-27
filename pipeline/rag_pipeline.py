import sys
import os

# Add the parent directory (RAGImplementation) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from retriever.retriever import Retriever
from generator.generator import Generator
from generator.prompt_templates import create_prompt

class RAGPipeline:
    def __init__(self, retriever_model, generator_model):
        self.retriever = Retriever(retriever_model)
        self.generator = Generator(generator_model)

    def run(self, query, file_path, top_k=5):
        self.retriever.index_documents(file_path)
        documents = self.retriever.search(query, top_k)
        prompt = create_prompt(query, documents)
        return self.generator.generate(prompt)