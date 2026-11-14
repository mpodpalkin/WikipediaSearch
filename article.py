from dataclasses import dataclass

@dataclass
class Article:
    page_id: int
    title: str
    snippet: str