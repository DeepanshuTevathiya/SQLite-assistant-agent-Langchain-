from dataclasses import dataclass
from langchain_community.utilities import SQLDatabase

@dataclass
class RuntimeContext:
    db: SQLDatabase