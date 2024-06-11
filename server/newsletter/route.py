from fastapi import APIRouter, HTTPException
from .session import add_email
from .schema import NewLetterSerializer

# nwl stands for newsletter
nwl = APIRouter()

@nwl.post('/newsletter/add')
def add(new : NewLetterSerializer):
    email = new.email
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    add_email(email)
    return {"message": "Email added successfully"}

