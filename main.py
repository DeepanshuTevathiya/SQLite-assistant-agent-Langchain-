from context import RuntimeContext
from langchain_community.utilities import SQLDatabase
from agent import main_agent


db = SQLDatabase.from_uri("sqlite:///database/Chinook_Sqlite.sqlite")

context = RuntimeContext(db=db)

agent = main_agent()

response = agent.stream(
    {"messages":"how recod sold in total according to the database"},
    stream_mode="values",
    context=context
)

for step in response:
    step["messages"][-1].pretty_print()