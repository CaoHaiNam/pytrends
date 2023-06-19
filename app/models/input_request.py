from pydantic import BaseModel

class InputRequest(BaseModel):
    keyword: str