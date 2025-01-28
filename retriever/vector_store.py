import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        """Initializes the FAISS index.

        Args:
            dim (int): Number of features in each vector being indexed 
            searched in the FAISS vector store.
        """
        self.index = faiss.IndexFlatL2(dim) # Stores the indexed vectors
        self.data = []  # Stores original text content for reference

    def add_vectors(self, vectors: list[list[float]], documents: list[str]):
        """Adds the vectors to index and corresponding document's chunk to data.

        Args:
            vectors (list[list[float]]): Embeddings of documents.
            documents (list[str]): Text contents of documents, each item represent one chunk.
        """
        self.index.add(np.array(vectors))
        self.data.extend(documents)

    def search(self, query_vector: list[list[float]], top_k=5) -> list:
        """Search for the vectors in index that match with query vector.

        Args:
            query_vector (list[list[float]]): Reference vector to make search.
            top_k (int, optional): Number of top matches to look for.

        Returns:
            list: Returns top matched text contents.
        """

        distances, indices = self.index.search(np.array([query_vector]), top_k)
        results = [self.data[i] for i in indices[0]]
        return results 
    