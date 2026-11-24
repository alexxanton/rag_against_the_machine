from typing import Optional
from .pipeline_step import PipelineStep


class Answer(PipelineStep):
    def __init__(
        self, k: Optional[int] = None, query: Optional[str] = None
    ) -> None:
        self.k = k or 0
        self.query = query or ""

    def execute(self) -> None:
        pass

    def execute_dataset(self, results_path: str, save_directory: str) -> None:
        pass
