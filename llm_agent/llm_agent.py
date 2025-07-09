import os
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferWindowMemory

from llm_agent.prompt_agent import reservation_prompt
from llm_agent.tools import (
    tool_query_hotel,
    tool_prediksi_batal,
    tool_simpan_reservasi,
)

# Load variabel dari .env
load_dotenv()
model_name = os.getenv("MODEL_NAME", "gemini-pro")

# Inisialisasi LLM Gemini
llm = ChatVertexAI(model=model_name, temperature=0.3)

# Tools yang akan digunakan agent
tools = [
    tool_query_hotel,
    tool_prediksi_batal,
    tool_simpan_reservasi,
]

# Memory untuk menyimpan histori percakapan
memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)

# Agent Executor: Agent dengan LLM + Tool + Prompt + Memory
agent_executor = initialize_agent(
    agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    memory=memory,
    verbose=True,
    agent_kwargs={
        "input_variables": ["input", "chat_history"],
        "prefix": reservation_prompt.template,
    },
)
