from common.auth import oauth2_bearer
from fastapi import HTTPException
from fastapi import status


def user_username_exists() -> HTTPException:
    username_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Podana nazwa użytkownika jest już zajęta.",
    )
    return username_exception


def user_must_be_admin() -> HTTPException:
    authority_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Brak uprawnień",
    )
    return authority_exception


def get_user_exception() -> HTTPException:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Nazwa użytkownika bądź hasło są nieprawidłowe",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credentials_exception


def token_exception() -> HTTPException:
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Nazwa użytkownika lub hasło są nieprawidłowe",
        headers={"WWW-Authenticate": oauth2_bearer},
    )
    return token_exception_response


def object_does_not_exist() -> HTTPException:
    object_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Nie możemy znaleźć tego czego szukasz :(",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return object_exception


def warsztat_re_opinion() -> HTTPException:
    object_exception = HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail="Wystawiłeś już opinie",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return object_exception


def could_not_mutate_address() -> HTTPException:
    address_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Wprowadzony adres nie może zostać skonwertowany na współrzędne geograficzne",
    )
    return address_exception


def mismatched_password() -> HTTPException:
    password_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Hasła się nie zgadzają",
    )
    return password_exception


def password_not_entered() -> HTTPException:
    password_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Brak hasła",
    )
    return password_exception


def identical_password() -> HTTPException:
    password_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Stare hasło nie może być takie samo jak nowe",
    )
    return password_exception
