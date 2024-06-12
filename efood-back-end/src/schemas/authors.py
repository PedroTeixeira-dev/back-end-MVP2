from pydantic import BaseModel, Field


class AuthorPostSchema(BaseModel):
    name: str = Field(None, min_length=1, max_length=200, description="name")
