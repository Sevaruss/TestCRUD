from pydantic import BaseModel, Field

class TestTabSchema(BaseModel):
    name: str = Field(..., max_length=100)
    descr: str = Field(..., max_length=255)

class TestTabDB(TestTabSchema):
    id: int