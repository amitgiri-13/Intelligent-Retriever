# Intelligent Retriever - AI-Powered Document Search

This project is a great starting point for anyone looking to understand the powerful Retrieval-Augmented Generation (RAG) architecture. It uses AI to retrieve relevant content from PDF documents and generate insightful answers with Google's Gemini model. It's a simple yet effective way to explore how RAG works. If you're interested in diving into the world of AI, give this project a try and start exploring the potential of RAG!

![What is RAG? ](https://github.com/amitgiri-13/Intelligent-Retriever/blob/main/ReadingResources/rag_notes.pdf)

## Preview
![image](https://github.com/user-attachments/assets/67fbbc3b-0a3d-4129-9bb6-de3a545a2a9a)

## Retrieval Augmented Generation (RAG) Architecture
  RAG (Retrieval-Augmented Generation) improves AI responses by retrieving relevant information from stored documents. A retriever searches a vector store, where documents are stored as numerical vectors using an embedding model. The retrieved context   is combined with the user’s query to form a prompt for the LLM (Large Language Model), which generates a response. This process enhances accuracy, making user interactions more informative and reliable.

![image](https://github.com/user-attachments/assets/3689f957-f705-45d5-8965-0ada749cdd29)
### Working of this Architecture
    1. User Query: The user submits a question or prompt.
    2. Context Retrieval: The system searches an external database (such as a vector store, document repository, or knowledge base) to find relevant documents based on the query.
    3. Context Augmentation: The retrieved documents are directly added to the user’s original query without additional filtering or ranking.
    4. Prompt Formation: The combined query and retrieved context are formatted into a single prompt.
    5. LLM Response Generation: The LLM processes the prompt and generates a response based on both the query and the retrieved contex.

## Features

- Retrieve relevant content from uploaded PDFs using a sentence-transformer model.

- Generate answers using Google's gemini-1.5-flash model.

- Interactive UI built with Streamlit for seamless user experience.

- Supports PDF documents and allows users to ask questions about their contents.

## Installation

Follow these steps to set up and run the project on your local machine.

1. Clone the Repository
```bash
git clone https://github.com/amitgiri-13/Intelligent-Retriever.git
cd Intelligent-Retriever
```

2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Set Up API Key

- Create a .env file in the root directory and add your Google API key:

- API_KEY=your_google_api_key_here. [Get Google AI Studio API Key (free tier works great for this project) ](https://aistudio.google.com/apikey)


5. Run the Application
```bash
streamlit run app.py
```
## How It Works

- Upload a PDF file via the Streamlit web interface.

- Enter a query related to the document.

- The system retrieves relevant content using a pre-trained sentence-transformer model.

- The Gemini model generates a response based on the retrieved content.

- The result is displayed on the UI.
  
### Workflow
![rag_implementation_workflow](https://github.com/user-attachments/assets/019f74b4-bc87-43fb-8f03-d45a2dbce786)

## Project Structure
```bash
IntelligentRetriever
├── data
│   ├── corpus
│       ├── document1.pdf
│       └──document2.pdf
├── retriever
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── retriever.py
│   └── vector_store.py
├── generator
│   ├── generator.py
│   ├── __init__.py
│   └── prompt_templates.py
├── pipeline
│   ├── __init__.py
│   └── rag_pipeline.py
├── config
│   └── rag_config.yaml
├── main.py
├── gui.py
├── tests
├── README.md
├── requirements.txt
├── LICENSE
├── rag_pipeline.log
```
[ Visit For Detail Workflow ](https://github.com/amitgiri-13/RAGImplementation/blob/main/Workflow.md)

## Configuration

- Modify the config/rag_config.yaml file to adjust settings:
```bash
rag_model: "sentence-transformers/all-MiniLM-L6-v2"
gen_model: "gemini-1.5-flash"
file_path: "data/corpus/sample.pdf"
top_k: 5
```

### Logging

- All logs are saved in rag_pipeline.log for debugging and monitoring.

## Future Improvements

- Support for multiple file formats (e.g., TXT, DOCX)

- Improve retrieval accuracy with better chunking techniques

- Deploy as a web service for broader accessibility

## Contribution
Any contribution  to this project is appreciated! If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request. Please ensure that your code follows the project's coding standards and includes relevant tests or documentation updates.

Thank you for your interest in contributing!

## License

This project is licensed under the MIT License.

Contact

For any issues or suggestions, feel free to reach out!
