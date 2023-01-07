from json import dumps as json

from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse


APP_JSON = "application/json"


def raise_http_exception(message: str, status_code: int = 400) -> None:
    raise HTTPException(
        status_code=status_code,
        detail={
            "msg": message
        }
    )


def get_html_response(
        status_code: int,
        content: dict,
        media_type: str = APP_JSON
) -> HTMLResponse:
    return HTMLResponse(
        status_code=status_code,
        content=json(content, indent=4),
        media_type=media_type
    )
