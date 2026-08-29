from pydantic import BaseModel ,EmailStr,StringConstraints
from datetime import datetime
from typing import Annotated

chek_password_lengh=Annotated[str,StringConstraints(min_length=8)]
class UserCreate(BaseModel):
    email:EmailStr
    password:chek_password_lengh
  
class UserLogin(BaseModel):
    email:EmailStr
    password:chek_password_lengh


class UserUpdate(BaseModel):
    password_hash:str|None=None
  


class UserResponse(BaseModel):

    model_config={"from_attributes":True}
    id:str
    email:EmailStr
    created_at:datetime
    access_token:str
    refresh_token:str