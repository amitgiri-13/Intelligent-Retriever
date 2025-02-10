from sentence_transformers import SentenceTransformer
from .vector_store import VectorStore
from .preprocessing import  read_pdf, preprocess_text

class Retriever:
    """ Index the document and help to retrieve the content that best matches the query.
    """
    def __init__(self, model_name="paraphrase-MiniLM-L6-v2",dim=384):
        """Initialize the model and vector_store.

        Args:
            model_name (str, optional): Model used for embeddings. Defaults to "paraphrase-MiniLM-L6-v2".
            dim (int, optional): Dimension for the vector store. Defaults to 384.
        """
        self.model = SentenceTransformer(model_name)
        self.vector_store = VectorStore(dim)

    def index_documents(self, file_path: str):
        """Index the document.

        Args:
            file_path (str): Path of the file to index.
        """
        raw_text = read_pdf(file_path)
        preprocessed_text = preprocess_text(raw_text)
        chunks = self.split_into_chunks(preprocessed_text)
        embeddings = self.model.encode(chunks)
        self.vector_store.add_vectors(embeddings, chunks)

    def split_into_chunks(self, text: str, chunk_size=200) ->list[str]:
        """Split the text into chunks.

        Args:
            text (str): Text data.
            chunk_size (int, optional):Size of the chunk to create. Defaults to 200.

        Returns:
            list[str]: List of chunks of given text data.
        """
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    def search(self, query:str, top_k=5) -> list[str]:
        """Search the content based on the query.

        Args:
            query (str): Query of the user.
            top_k (int, optional):Number of top matches to return. Defaults to 4.

        Returns:
            list[str]: List of chunks of document that matches with query most.
        """
        query_vector = self.model.encode([query])[0]
        return self.vector_store.search(query_vector, top_k)

# Testing
if __name__ == "__main__":
    file = "/home/amit/Repositories/PythonStuffs/ArtificialIntelligence/RAGImplementation/data/corpus/raj_meera.pdf"
    retriever = Retriever()
    retriever.index_documents(file)
    
    query = "why could not raj confess to meera?"
    result = retriever.search(query=query)
    print(result)
    
