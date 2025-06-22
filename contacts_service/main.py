from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

class PhoneType(str, Enum):
    mobile = "mobile"
    landline = "landline"
    commercial = "commercial"

class Category(str, Enum):
    family = "family"
    personal = "personal"
    commercial = "commercial"

class Phone(BaseModel):
    number: str
    type: PhoneType

class ContactIn(BaseModel):
    name: str
    phones: List[Phone]
    category: Category

class Contact(ContactIn):
    id: int

app = FastAPI(title="Contacts Service")

# armazenamento simples em memória
_db: dict[int, Contact] = {}
_counter = 1

@app.post("/contacts", response_model=Contact, status_code=201)
def create_contact(payload: ContactIn):
    global _counter
    contact = Contact(id=_counter, **payload.dict())
    _db[_counter] = contact
    _counter += 1
    return contact

@app.get("/contacts/{contact_id}", response_model=Contact)
def get_contact(contact_id: int):
    contact = _db.get(contact_id)
    if not contact:
        raise HTTPException(404, detail="Contact not found")
    return contact

@app.get("/contacts", response_model=List[Contact])
def list_contacts():
    return list(_db.values())