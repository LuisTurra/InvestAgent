from pydantic import BaseModel


class Report(BaseModel):

    recommendation: str
    risk: str
    confidence: int
    reasoning: str