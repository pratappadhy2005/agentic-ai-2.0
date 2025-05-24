from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr  # type: ignore

app = FastAPI()


class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str


class Settings(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = 'admin@chai.com'


def get_settings():
    return Settings()


@app.post("/signup")
async def signup(user: UserSignup):
    return {"message": f'User {user.username} created'}


@app.get("/settings")
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
