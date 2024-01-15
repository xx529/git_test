from pydantic import BaseModel
from typing import Optional


class Test(BaseModel):
    data: str
    start: Optional[str]
    end: Optional[str]
