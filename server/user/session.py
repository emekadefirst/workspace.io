from models import User
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from passlib.context import CryptContext
from .database import engine

# Dependency for creating a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    return pwd_context.hash(password)


async def create_user(username: str, email: str, password: str):
    hashed_password = hash_password(password)
    async with SessionLocal() as session:
        user = User(username=username, email=email, hashed_password=hashed_password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def get_user_by_username(username: str):
    async with SessionLocal() as session:
        return await session.exec(User).where(User.username == username).first()


async def get_user_by_id(user_id: int):
    async with SessionLocal() as session:
        return await session.get(User, user_id)


async def delete_user(user_id: int):
    async with SessionLocal() as session:
        user = await session.get(User, user_id)
        if user:
            session.delete(user)
            await session.commit()
            return f"User with ID {user_id} deleted successfully"
        return None
