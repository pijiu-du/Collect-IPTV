
import os
from pathlib import Path
from wsgiref.util import FileWrapper

BASE_DIR = Path(__file__).resolve().parent

def application(environ, start_response):
    path = environ.get("PATH_INFO", "/").lstrip("/")

    if not path:
        path = "index.html"

    target = (BASE_DIR / path).resolve()

    if not target.is_relative_to(BASE_DIR) or not target.is_file():
        start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
        return [b"Not Found"]

    content_type = "application/octet-stream"
    if target.suffix == ".m3u":
        content_type = "audio/x-mpegurl"
    elif target.suffix == ".m3u8":
        content_type = "application/vnd.apple.mpegurl"
    elif target.suffix == ".txt":
        content_type = "text/plain; charset=utf-8"

    start_response("200 OK", [("Content-Type", content_type)])
    return FileWrapper(open(target, "rb"))

