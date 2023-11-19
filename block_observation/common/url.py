from urllib.parse import urlparse
from typing import Optional


def get_url(
    url: str,
    path: Optional[str] = None,
    query: Optional[dict] = None,
) -> str:
    u = urlparse(url)

    if path is not None:
        u = u._replace(path=path)

    if query is not None:
        q = "&".join([f"{k}={v}" for k, v in query.items()])
        u = u._replace(query=q)

    return u.geturl()
