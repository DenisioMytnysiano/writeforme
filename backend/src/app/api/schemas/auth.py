from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    fingerprint: str


class TokenResponse(BaseModel):
    access_token: str


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class RefreshTokenRequest(BaseModel):
    fingerprint: str
