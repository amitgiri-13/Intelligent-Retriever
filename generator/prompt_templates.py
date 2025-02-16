def create_prompt(query: str, context: str):
    """Prompt template.

    Args:
        query (str): User's prompt.
        context (str): Retrieved context from document.

    Returns:
        _type_: Custom prompt for  llm.
    """
    context = f"\nBased on the context answer query like wise human\n"
    context = context.join(context)
    return f"Context:\n{context}\nQuery:\n{query}\nAnswer:"
