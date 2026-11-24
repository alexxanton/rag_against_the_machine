from .pipeline_step import PipelineStep
from typing import Optional


class Search(PipelineStep):
    def __init__(self, k: int, query: Optional[str] = None) -> None:
        self.k = k
        self.query = query or ""

    def execute(self) -> None:
        pass

    def execute_dataset(self, dataset_path: str, save_directory: str) -> None:
        pass
        #print(save_directory)
