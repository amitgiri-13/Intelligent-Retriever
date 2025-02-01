# IntelligentRetriever Workflow

1. Data Preparation (data/)
    - Corpus (data/corpus/): The raw PDF documents (document1.pdf, document2.pdf, etc.) are stored in the corpus directory.
    - Embeddings (data/embeddings/): The embeddings (vectorized representations) of the documents are generated and stored       here     after the preprocessing step.
    -  Processed (data/processed/): Any processed or cleaned data, such as text extracted from the PDFs, is saved here.

2. Document Preprocessing (retriever/preprocessing.py)
    - Extract text and metadata from the raw PDF documents.
    - Clean and preprocess the text to remove irrelevant data (e.g., formatting, headers, footers).
    - Split the text into chunks (e.g., paragraphs or sentences) for more efficient retrieval.

3. Vectorization and Storage (retriever/vector_store.py)
    - The preprocessed text is vectorized using an embedding model (e.g., using libraries like HuggingFace or OpenAI's models).
    - Store the vectorized data in a vector store or database for fast retrieval.

4. Document Retrieval (retriever/retriever.py)
    - When a query is received, the retriever performs a similarity search against the stored embeddings to find the most relevant documents or document sections.
    - Retrieve the top-n relevant document chunks based on cosine similarity or another similarity metric.

5. Answer Generation (generator/generator.py)
    - The retrieved document chunks are passed to the generator.
    -  The generator uses a pre-trained model (like Google's Gemini or another transformer-based model) to generate a human-readable answer.
    - Prompt Templates (generator/prompt_templates.py): Templates for generating prompts are defined here. These templates can be customized depending on the query and the retrieved content.

6. RAG Pipeline Integration (pipeline/rag_pipeline.py)
    - The Retrieval-Augmented Generation (RAG) pipeline ties the retrieval and generation together.
    - This pipeline receives the user query, performs document retrieval using the retriever, and then generates the answer using the generator.
    - The final result (answer) is passed back to the user.

7. Configuration (config/rag_config.yaml)
    - Configuration settings (e.g., model parameters, number of retrieved documents, etc.) are stored here for easy access and management.
    - The YAML file helps in managing different environment settings like API keys, model selection, and retriever settings.

8. Main Execution (main.py)
    - This is the entry point of the application. It initiates the RAG pipeline based on user input, orchestrating the flow from document retrieval to answer generation.
    - The user query is passed to the pipeline, and the result is outputted (possibly printed or returned via an API).

9. Graphical User Interface (gui.py)
    - A simple GUI can be built here to allow users to interact with the IntelligentRetriever via a graphical interface.
        Users can upload documents, input queries, and view results from the RAG system.

10. Logs (rag_pipeline.log)
    - Logs are generated during execution to track errors, performance, and other important details during the RAG pipeline run. It helps in debugging and optimizing the workflow.

11. Documentation (README.md, LICENSE, Workflow.md)
    - The README file provides detailed instructions for setting up and using the IntelligentRetriever system.
    - The workflow.md has detailed workflow to understand and develop this project.
    - The LICENSE file defines the licensing terms under which the project is distributed.

12. Dependencies (requirements.txt)
    - All the dependencies required for running the project, such as libraries for PDF parsing, text processing, machine learning, and model handling, are listed here.

# Data Flow Overview:

1. User Query → Interface → Pipeline (rag_pipeline.py) → Retriever (retriever.py) → Document Retrieval → Embedding Search
2. Retriever → Top-N Relevant Chunks → Generator (generator.py) → Answer Generation
3. Generated Answer → Interface → GUI/Output Display

# Execution Workflow:

1. Start: User enters a query through GUI.
2. Document Retrieval: Preprocessed documents are searched for relevant information based on the query.
3. Answer Generation: Retrieved documents are passed to the generator to create a coherent and insightful response.
4. Display Result: The generated answer is displayed back to the user.

