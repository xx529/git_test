from pydantic import BaseModel


class Test(BaseModel):
    data: str
    start: str
    end: str = None
