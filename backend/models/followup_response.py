from pydantic import BaseModel


class FollowupResponse(BaseModel):
    followup_type: str
    subject: str
    email_body: str
