from dotenv import load_dotenv
from langchain.agents import create_agent

from tools.schema import get_schema
from tools.tables import get_tables
from tools.execute_sql import execute_sql
from prompt import SYSTEM_PROMPT
from context import RuntimeContext

load_dotenv()

def main_agent():
    agent = create_agent(
        model="gpt-5-mini-2025-08-07",
        tools=[execute_sql, get_schema, get_tables],
        system_prompt=SYSTEM_PROMPT,
        context_schema=RuntimeContext,
    )

    return agent

