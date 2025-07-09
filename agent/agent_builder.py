import os
import vertexai
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_google_vertexai import ChatVertexAI

from .prompt_template import recommendation_template

# 🔁 Load .env
load_dotenv()

# 🔧 Inisialisasi Vertex AI
project = os.getenv("GEMINI_PROJECT_ID")
location = os.getenv("GEMINI_LOCATION")
model_name = os.getenv("MODEL_NAME", "gemini-pro")

vertexai.init(project=project, location=location)

# 🧱 Skema output rekomendasi
class Rekomendasi(BaseModel):
    nama: str
    harga: int
    diterima: bool
    alasan: str

class OutputModel(BaseModel):
    rekomendasi: List[Rekomendasi]

# 🔗 Build agent
llm = ChatVertexAI(model=model_name, temperature=0.3)
parser = PydanticOutputParser(pydantic_object=OutputModel)

def build_agent():
    """
    Mengembalikan chain agent LangChain yang terdiri dari prompt, LLM, dan parser output.
    """
    return recommendation_template | llm | parser
