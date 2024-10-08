from pydantic import BaseModel
from typing import List, Dict

class PollCreate(BaseModel):
    title: str
    options: List[str]

class VoteCreate(BaseModel):
    poll_id: int
    option: str

class PollResults(BaseModel):
    poll_id: int
    results: Dict[str, int]
