# Assign2_Resume-Information-Extractor
## 📄 Resume Information Extractor

This project is an AI-powered Resume Information Extractor that converts unstructured resume PDFs into structured JSON format using LangChain, Ollama (Llama3 – Local LLM), JsonOutputParser, and Pydantic schema validation.

The system first extracts raw text from a PDF using PyPDFLoader, then applies structured prompting with format instructions to guide the LLM in generating a consistent JSON response. The output is validated using a Pydantic schema to ensure correctness and reliability.

It extracts key candidate details such as:

1. Full Name

2. Email Address

3. Technical Skills

4. Total Years of Experience

5. Education Details

The entire pipeline runs locally using Ollama, eliminating the need for external APIs or API keys. This project demonstrates structured output parsing, schema validation, and building a modular LLM-powered data extraction system suitable for real-world automation tasks.
