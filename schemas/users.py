from pydantic import BaseModel


class UserBase(BaseModel):
    email = str
    username = str

class UserCreate(UserBase):
    password = str

class User(UserBase):
    id = int

    class config:
        orm_mode = True