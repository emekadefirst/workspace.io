from pydantic import BaseModel

class NewLetterSerializer(BaseModel):
    email: str 