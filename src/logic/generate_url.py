import hashlib
from src.database.localdao import LocalDAO


def generate_tiny_url(long_url: "str", local_dao: "LocalDAO"):
    tiny_url = hashlib.md5(bytes(long_url, "utf-8")).hexdigest()
    local_dao.put(tiny_url, long_url)
    return tiny_url
