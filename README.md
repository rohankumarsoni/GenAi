# Generative AI with LangChain

A hands-on repository for learning and implementing **Generative AI applications using LangChain, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Vector Databases**.

This repository contains practical implementations of core LangChain concepts, progressing from basic LLM interactions to building complete **RAG-based applications**.

---

## Topics Covered

### 1. LangChain Models

Working with different LLM providers and model integrations.

* OpenAI
* Google Gemini
* Anthropic
* Hugging Face
* Chat Models
* LLM APIs

### 2. Prompt Engineering

Building reusable and dynamic prompts using LangChain.

* PromptTemplate
* ChatPromptTemplate
* MessagesPlaceholder
* Dynamic prompts
* Chat history

### 3. Structured Output

Generating predictable and structured responses from LLMs.

* Pydantic models
* TypedDict
* JSON output
* `with_structured_output()`
* Function calling

### 4. Output Parsers

Converting LLM responses into structured formats.

* StringOutputParser
* JsonOutputParser
* StructuredOutputParser
* PydanticOutputParser

### 5. LangChain Chains

Combining prompts, models and parsers into reusable pipelines.

```text
Prompt → LLM → Output Parser
```

### 6. LangChain Runnables

Understanding LangChain's Runnable architecture and LCEL.

Topics include:

* RunnableSequence
* RunnableParallel
* RunnablePassthrough
* RunnableLambda
* RunnableBranch
* LCEL (LangChain Expression Language)

### 7. Document Loaders

Loading external data into LangChain applications, including PDFs and other text sources.

### 8. Text Splitters

Breaking large documents into smaller chunks suitable for LLM and RAG applications.

* RecursiveCharacterTextSplitter
* Character-based splitting
* Chunk size
* Chunk overlap
* Semantic chunking concepts

### 9. Vector Stores

Converting documents into embeddings and storing them for semantic search.

```text
Documents
    ↓
Text Chunks
    ↓
Embeddings
    ↓
Vector Store
    ↓
Similarity Search
```

### 10. Retrievers

Retrieving the most relevant document chunks for a user query.

* Similarity search
* Top-K retrieval
* Vector store retrievers
* Semantic retrieval

---

# YouTube RAG Chatbot

The repository contains an end-to-end **Retrieval-Augmented Generation (RAG) project** that allows users to ask questions about a YouTube video.

## Architecture

```text
YouTube Video
      ↓
Video Transcript
      ↓
Text Splitting
      ↓
Document Chunks
      ↓
OpenAI Embeddings
      ↓
FAISS Vector Database
      ↓
Retriever
      ↓
Relevant Chunks
      ↓
Prompt + Context
      ↓
LLM
      ↓
Answer
```

## How It Works

### 1. Extract YouTube Transcript

The transcript is retrieved using `youtube-transcript-api`.

### 2. Split Transcript

The transcript is divided into smaller chunks using `RecursiveCharacterTextSplitter`.

### 3. Generate Embeddings

Each chunk is converted into a numerical vector representation using an embedding model such as:

```python
OpenAIEmbeddings(
    model="text-embedding-3-small"
)
```

### 4. Store Embeddings in FAISS

The embeddings are indexed using **FAISS** for efficient vector similarity search.

```python
vector_store = FAISS.from_documents(
    chunks,
    embeddings
)
```

### 5. Retrieve Relevant Context

A retriever finds the most relevant chunks for the user's question.

```python
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)
```

### 6. Generate the Answer

The retrieved chunks are combined into context and passed along with the user's question to the LLM to generate a grounded answer.

---

# Tech Stack

* Python
* LangChain
* OpenAI
* Google Gemini
* Anthropic
* Hugging Face
* FAISS
* Scikit-learn
* NumPy
* YouTube Transcript API
* Python Dotenv

---

# Repository Structure

```text
GenAi/
│
├── 1.Langchain_Models/
├── 2.Langchain_prompts/
├── 3.Langchian_structured_output/
├── 4.Langchain_output_parsers/
├── 5.langchain_chains/
├── 6.langchain_runnables/
├── 7.langchain_document_loaders_main/
├── 8.langchain_text_splitters/
├── 9.Vector_Stores_in_LangChain/
├── 10.Retrievers/
├── 11.RAG_Proj_youtube_chatbot/
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/rohankumarsoni/GenAi.git
cd GenAi
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

Never commit your `.env` file or API keys to GitHub.

---

# Key Concepts Demonstrated

```text
LLMs
 ↓
Prompt Engineering
 ↓
Structured Outputs
 ↓
Output Parsers
 ↓
Chains
 ↓
Runnables / LCEL
 ↓
Document Loading
 ↓
Text Chunking
 ↓
Embeddings
 ↓
Vector Databases
 ↓
Retrieval
 ↓
RAG Applications
```

---

# Purpose

This repository is designed as a practical learning resource for:

* Generative AI
* LangChain
* LLM application development
* Retrieval-Augmented Generation (RAG)
* Semantic search
* Vector databases
* AI/GenAI interview preparation

The goal is to move from understanding individual LangChain components to building complete **LLM-powered applications**.

---

# Credits

A significant part of the learning and concepts implemented in this repository is inspired by the **CampusX YouTube channel** and the excellent educational content created by **Nitish Singh**.

Special thanks to **Nitish Singh and CampusX** for providing clear, practical, and accessible content on Generative AI, LangChain, Machine Learning, and Data Science.

This repository is created for **learning and practice purposes**, based on concepts learned from these resources along with my own implementations and experimentation.

---

## Author

**Rohan Kumar Soni**

GitHub: `rohankumarsoni`
