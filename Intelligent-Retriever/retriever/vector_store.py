import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim) # Stores the indexed vectors
        self.data = []  # Stores original text content for reference

    def add_vectors(self, vectors: list[list[float]], chunk: list[str]):
        self.index.add(np.array(vectors))
        self.data.extend(chunk)

    def search(self, query_vector: list[list[float]], top_k=3) -> list:
        distances, indices = self.index.search(np.array([query_vector]), top_k)
        results = [self.data[i] for i in indices[0]]
        return results 
    