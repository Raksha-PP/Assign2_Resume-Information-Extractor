from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import PyPDFLoader
from pydantic import BaseModel, Field
import json


class ResumeSchema(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address")
    skills: list[str] = Field(description="List of technical skills")
    experience_years: int = Field(description="Total years of experience")
    education: list[str] = Field(description="Educational qualifications")


parser = JsonOutputParser(pydantic_object=ResumeSchema)


prompt = PromptTemplate(
    template="""
You are an AI resume information extractor.

Extract the following structured information from the resume text.

Resume Text:
{resume_text}

{format_instructions}

IMPORTANT:
- Return ONLY valid JSON.
- Do not include explanations.
- If any field is missing, return null or empty list.
""",
    input_variables=["resume_text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


model = ChatOllama(
    model="llama3",
    temperature=0
)


chain = prompt | model | parser


try:
    loader = PyPDFLoader("resume.pdf")
    documents = loader.load()
except Exception as e:
    print("Error loading PDF:", e)
    exit()

resume_text = "\n".join([doc.page_content for doc in documents])

if not resume_text.strip():
    print("Resume text is empty. Check your PDF.")
    exit()


try:
    result = chain.invoke({"resume_text": resume_text})
    print("\n✅ Extracted Resume Data:\n")
    print(json.dumps(result, indent=4))

except Exception as e:
    print("\n❌ Parsing Error:")
    print(str(e))
