from fastapi import APIRouter

router = APIRouter()


@router.get("/.well-known/acme-challenge/{token}")
async def acme_challenge(token: str):
    return "This is a test"
