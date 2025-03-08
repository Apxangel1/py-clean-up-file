from typing import Any
import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name
        self.file = None

    def __enter__(self) -> Any:
        return self

    def __exit__(self) -> None:
        os.remove(self.filename)
