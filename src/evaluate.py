from typing import Optional
from .pipeline_step import PipelineStep


class Evaluate(PipelineStep):
    def execute_dataset(self, results_path: str, save_directory: str) -> None:
        pass
