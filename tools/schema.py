from langchain.tools import tool
from langgraph.runtime import get_runtime
from context import RuntimeContext

@tool
def get_schema(table_name:str):
    """Provide the schema of specific table in database"""
    runtime = get_runtime(RuntimeContext)
    db = runtime.context.db

    try:
        return db.get_table_info([table_name])
    except Exception as e:
        raise ValueError(f"Error!: {e}")