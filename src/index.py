from .pipeline_step import PipelineStep


class Index(PipelineStep):
    def __init__(self, max_chunk_size: int) -> None:
        self.max_chunk_size = max_chunk_size

    def execute(self) -> None:
        print(self.max_chunk_size)

    def execute_dataset(self, p1: str, p2: str) -> None:
        pass
