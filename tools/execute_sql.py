from langchain.tools import tool
from langgraph.runtime import get_runtime
from context import RuntimeContext

@tool
def execute_sql(query:str):
    """Execute the given SQLite queries. and validate it"""
    runtime = get_runtime(RuntimeContext)
    db = runtime.context.db

    word = query.split()[0]
    if word.lower() == "select":
        try:
            return db.run(query)
        except Exception as e:
            return f"Error!: {e}"
    else:
        return "Error!: only SELECT query allowed"