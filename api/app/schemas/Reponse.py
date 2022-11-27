from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')

class Reponse(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
