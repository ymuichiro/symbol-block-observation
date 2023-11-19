from dotenv import load_dotenv
from .url import get_url
import os

load_dotenv()

__NODE_SSL: bool = bool(os.environ.get("NODE_SSL", "True"))
NODE_HTTP_URL: str = os.environ.get("NODE_HOST", "localhost:3001")
NODE_WS_URL: str = os.environ.get("NODE_HOST", "localhost:3001")
NOTIFICATION_HTTP_URL: str = os.environ.get("NOTIFICATION_URI", "http://localhost:3000")

if __NODE_SSL:
    NODE_HTTP_URL = "https://" + NODE_HTTP_URL
    NODE_WS_URL = get_url("wss://" + NODE_WS_URL, path="/ws")
else:
    NODE_HTTP_URL = "http://" + NODE_HTTP_URL
    NODE_WS_URL = get_url("ws://" + NODE_WS_URL, path="/ws")
