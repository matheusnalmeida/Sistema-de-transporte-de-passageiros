class Cache:
    _instance = None

    def __init__(self):
        self.data = {}

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance