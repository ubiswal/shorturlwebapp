from src.database.localdao import LocalDAO


def get_full_url(tiny_url: "str", local_dao: "LocalDAO"):
    return local_dao.get(tiny_url)

