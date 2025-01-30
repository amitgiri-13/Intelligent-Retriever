def create_prompt(query: str, documents: str):
    """Prompt template.

    Args:
        query (str): User's prompt.
        documents (str): Data from RAG.

    Returns:
        _type_: Custom prompt to actually feed to llm.
    """
    context = f"\nBased on the context answer query like wise human\n"
    context = context.join(documents)
    return f"Context:\n{documents}\nQuery:\n{query}\nAnswer:"
