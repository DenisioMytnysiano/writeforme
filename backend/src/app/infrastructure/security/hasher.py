from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    def hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify(self, original: str, hashed: str) -> bool:
        return pwd_context.verify(original, hashed)
