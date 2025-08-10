from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import List

#Create the FASTAPI instance
app = FastAPI(title="My FastAPI Application", version="1.0.0")

# store the registered users
registered_users = []

class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="The username of the user")
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=100, description="The full name of the user")
    password: str = Field(..., min_length=6, max_length=100, description="The password of the user")
    
# Get user detail
class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    registered: bool

@app.post("/register", response_model=UserResponse, status_code=201)
def register_user(user: UserRegister):
    if user.email in [u.email for u in registered_users]:
        return {"error": "Email already registered"}
    registered_users.append({
        
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "password": user.password
    })
    return UserResponse(**user.dict(), registered=True)
@app.get("/users", response_model=List[UserResponse])
def get_users():
    return [UserResponse(**user, registered=True) for user in registered_users]
