from pydantic import BaseModel, EmailStr, Field

class StudentBase(BaseModel):
    name: str
    email: EmailStr                                          # Validates email format
    age: int = Field(gt=0, description="Age must be positive")  # Must be positive
    course: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True
