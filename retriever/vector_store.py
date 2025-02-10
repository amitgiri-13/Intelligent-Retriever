import faiss
import numpy as np

class VectorStore:
    """Vector Store to store the embeddings and corresponding data chunk.
    """
    def __init__(self, dim: int):
        """Initializes the FAISS index.

        Args:
            dim (int): Number of features in each vector being indexed and
            searched in the FAISS vector store.
        """
        self.index = faiss.IndexFlatL2(dim) # Stores the indexed vectors
        self.data = []  # Stores original text content for reference

    def add_vectors(self, vectors: list[list[float]], chunk: list[str]):
        """Adds the vectors to index and corresponding text chunk to data.

        Args:
            vectors (list[list[float]]): Embeddings of the text data chunk.
            chunk (list[str]): Actual chunk of the text data.
        """
        self.index.add(np.array(vectors))
        self.data.extend(chunk)

    def search(self, query_vector: list[list[float]], top_k=3) -> list:
        """Search for the top vectors in index that match with query vector.

        Args:
            query_vector (list[list[float]]): Reference vector to make search.
            top_k (int, optional): Number of top matches to look for.

        Returns:
            list: Returns top matched text contents.
        """

        distances, indices = self.index.search(np.array([query_vector]), top_k)
        results = [self.data[i] for i in indices[0]]
        return results 
    