from pydantic import BaseModel

class UserSignUp(BaseModel):
    email:str
    password:str
    class Config:
        json_schema_extra = {
            "example":{
            "email": "sample@gmail.com",
            "password": "sample_pass"
            }
        }

class UserLogin(BaseModel):
    email:str
    password:str
    class Config:
        json_schema_extra = {
            "example":
                {
                    "email": "sample@gmail.com",
                    "password": "sample_pass"
                }
        }