import os
from typing import Generator
from typing import Union

from common.auth import oauth2_bearer
from db.session import SessionLocal
from dotenv import load_dotenv
from fastapi import Depends
from jose import jwt
from jose import JWTError
from models.user import User
from sqlalchemy.orm import Session

from .exceptions import get_user_exception, user_must_be_admin

load_dotenv()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_current_user(
    token: str = Depends(oauth2_bearer), db: Session = Depends(get_db)
) -> Union[User, Exception]:
    try:
        payload = jwt.decode(token, os.getenv("TOKEN"), algorithms=[os.getenv("ALGORYTM")])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise get_user_exception()
    except JWTError:
        raise get_user_exception()

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise get_user_exception()
    return user


def get_admin_user(user: User):
    if user.is_admin:
        return user

    raise user_must_be_admin()
