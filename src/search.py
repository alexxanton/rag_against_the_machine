from .pipeline_step import PipelineStep
from typing import Optional


class Search(PipelineStep):
    def __init__(self, k: int, query: Optional[str] = None) -> None:
        self.k = k
        self.query = query or ""

    def execute(self) -> None:
        if not self._is_valid("query", str):
            return
        if not self._is_valid("k", int):
            return

    def execute_dataset(self, dataset_path: str, save_directory: str) -> None:
        if not self._is_valid("k", int):
            return
        print(self.k)
