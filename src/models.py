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

class EmailRequest(BaseModel):
    email: str

class LoginRequest(BaseModel):
    email: str
    password: str | None = None
    login_type: str  # 'email' or 'google'
    id_token: str | None = None
    name: str | None = None
    google_id: str | None = None
