from pydantic import BaseModel

class Outreach(BaseModel):
    email_subject: str
    email_body: str
    linkedin_message: str
    call_opener: str
    executive_summary: str