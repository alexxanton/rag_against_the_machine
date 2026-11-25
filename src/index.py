from .pipeline_step import PipelineStep
from .file import File
from pathlib import Path


class Index(PipelineStep):
    """Loads the corpus to split it into chunks and indexes them."""

    def __init__(self, max_chunk_size: int) -> None:
        """Initialize the index class."""
        self.max_chunk_size = max_chunk_size

    def _load_corpus(self) -> None:
        root = Path("/data/raw")
        files = [
            File(f) for f in root.rglob("*")
            if f.suffix in {".py", ".md"}
        ]
        print(files)

    def execute(self) -> None:
        if not self._is_valid("max_chunk_size", int):
            return
        self._load_corpus()

    def execute_dataset(self, p1: str, p2: str) -> None:
        raise NotImplementedError
