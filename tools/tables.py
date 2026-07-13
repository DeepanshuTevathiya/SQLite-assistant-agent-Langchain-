from langchain.tools import tool
from langgraph.runtime import get_runtime
from context import RuntimeContext

@tool
def get_tables():
    """Provide the name of all tables in the database."""
    runtime = get_runtime(RuntimeContext)
    db = runtime.context.db

    try:
        return db.get_usable_table_names()
    except Exception as e:
        raise ValueError(f"Error!: {e}")