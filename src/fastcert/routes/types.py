from typing import Generic, Text, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    success: bool = Field(True, description="Whether the request was successful")
    error_code: Text = Field(
        None, description="Error code if the request was unsuccessful"
    )
    error_message: Text = Field(
        None, description="Error message if the request was unsuccessful"
    )
    data: T = Field(None, description="Data returned by the request")
