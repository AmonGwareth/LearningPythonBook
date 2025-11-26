
class Client:

    def __init__(self):
        print("Setting up the client...")

    def query(self, **kwargs):
        print(f"Performing a query: {kwargs}")


class Manager:
    @property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)


class ManualCacheManager:
    @property  # setup the getter
    def client(self):
        if not hasattr(self, "_client"):
            self._client = Client()
        return self._client

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)


# smartest solution using functools
from functools import cached_property


class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)
