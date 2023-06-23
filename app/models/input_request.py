from pydantic import BaseModel
from typing import List

class InputRequest(BaseModel):
    keywords: List[str]

