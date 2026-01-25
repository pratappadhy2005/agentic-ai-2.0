# RAG Chat with Docs

This project demonstrates a Retrieval-Augmented Generation (RAG) application using ChromaDB and OpenAI. It allows you to chat with a set of news articles by retrieving relevant information from a vector database.

## Project Structure

- **`rag_app.ipynb`**: The main Jupyter Notebook containing the code to initialize the database, embed documents, and query the RAG system.
- **`news_articles_documents/`**: A directory containing the text files (news articles) used as the knowledge base.
- **`chroma_vdb_persistent_storage/`**: The persistent storage directory for the ChromaDB vector database.

## Prerequisites

To run this project, you need the following:

1.  **OpenAI API Key**: You need a valid OpenAI API key.
2.  **Python Libraries**: Install the required dependencies (you can use `pip`):
    ```bash
    pip install chromadb openai python-dotenv notebook
    ```

## Setup & Usage

1.  **Environment Variables**:
    - Create a `.env` file in the root of this directory (or ensure one exists).
    - Add your OpenAI API key:
      ```env
      OPENAI_API_KEY=your_api_key_here
      ```

2.  **Run the Notebook**:
    - Open `rag_app.ipynb` in Jupyter Notebook or VS Code.
    - Execute the cells to load documents, generate embeddings, and query the system.

## How it Works

1.  **Loading**: The notebook reads text files from the `news_articles_documents/` folder.
2.  **Embedding**: It uses OpenAI's embedding model (`text-embedding-3-small`) to convert text into vector embeddings.
3.  **Storage**: These embeddings are stored in ChromaDB (persisted in `chroma_vdb_persistent_storage/`).
4.  **Retrieval**: When you ask a question, the system finds the most relevant document chunks.
5.  **Generation**: The retrieved context is passed to an OpenAI LLM to generate an answer.
