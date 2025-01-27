def create_prompt(query: str, documents: str):
    """Prompt template

    Args:
        query (str): User's prompt.
        documents (str): Data from RAG.

    Returns:
        _type_: Returns actual prompt to feed to llm.
    """
    context = "\n".join(documents)
    return f"Context:\n{context}\nQuery:\n{query}\nAnswer:"
