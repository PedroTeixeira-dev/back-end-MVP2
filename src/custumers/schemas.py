from typing import Optional
from pydantic import BaseModel, Field


class CustumersPostSchema(BaseModel):
    email: str = Field(max_lenght=30, description="Email")
    name: str = Field(max_lenght=50, description="Name")
    cep: str = Field(max_lenght=8, description="CEP")
    uf: str = Field(max_lenght=10, description="State")
    city: str = Field(max_lenght=30, description="City")
    street: str = Field(max_lenght=40, description="Street")
    number: int = Field(max_lenght=10, description="Number")
    complement: Optional[str] = Field(None, max_lenght=100, description="Complement")


class CustumersResponseSchema(BaseModel):
    email: str = Field(max_lenght=30, description="Email")
    name: str = Field(max_lenght=50, description="Name")
    cep: str = Field(max_lenght=8, description="CEP")
    uf: str = Field(max_lenght=10, description="State")
    city: str = Field(max_lenght=30, description="City")
    street: str = Field(max_lenght=40, description="Street")
    number: int = Field(max_lenght=10, description="Number")
    complement: Optional[str] = Field(None, max_lenght=100, description="Complement")


class CustumerDeleteSchema(BaseModel):
    email: str = Field(..., max_length=30, description="Email")


class EmailPath(BaseModel):
    email: str = Field(..., description='email adress to search')
