import json
from pathlib import Path


class File:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
