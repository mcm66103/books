import requests

class GoogleBooks():
    BASE_URL = "https://www.googleapis.com/books/"
    VERSION = "v1/"

    @classmethod 
    def query_volumes(cls, q):
        return cls.get("volumes", q)

    @classmethod
    def volume_details(cls, id):
        return cls.get(f"volumes/{id}", None)

    @classmethod
    def get(cls, path, q):
        url = cls.build_url(path, q)
        return requests.get(url).json()

    @classmethod
    def build_url(cls, path, query):
        return f"{cls.BASE_URL}{cls.VERSION}{path}?q={query}"