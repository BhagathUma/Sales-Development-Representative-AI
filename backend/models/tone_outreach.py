from pydantic import BaseModel

class ToneOutreach(BaseModel):
    tone: str

    email_subject: str

    email_body: str

    linkedin_message: str