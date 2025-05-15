from typing import Text

from fastapi import APIRouter
from pydantic import BaseModel, Field

from .types import BaseResponse


class CertificateCreateRequest(BaseModel):
    domain: Text = Field(..., description="Domain name")


class CertificateCreateResponse(BaseModel):
    id: Text = Field(..., description="Certificate ID")


router = APIRouter()


@router.post("/certificates")
async def acme(
    request: CertificateCreateRequest,
) -> BaseResponse[CertificateCreateResponse]:
    pass
