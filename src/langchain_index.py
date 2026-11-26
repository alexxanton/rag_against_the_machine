import bm25s
from .pipeline_step import PipelineStep
from .file import File
from pathlib import Path
from langchain_text_splitters import (
    PythonCodeTextSplitter,
    RecursiveCharacterTextSplitter
)

class Index(PipelineStep):
    """Loads the corpus to split it into chunks and indexes them."""

    def __init__(self, max_chunk_size: int) -> None:
        """Initialize the index class."""
        self.max_chunk_size = max_chunk_size

    def _init_splitters(self) -> None:
        """Initialize the splitters."""
        self.py_splitter = PythonCodeTextSplitter(
            chunk_size=self.max_chunk_size,
            chunk_overlap=0,
            add_start_index=True
        )

        self.md_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.max_chunk_size,
            chunk_overlap=0,
            add_start_index=True
        )

    def _split_files(files) -> None:
        """Split the files into chunks."""

    def _load_corpus(self) -> None:
        """Load all the python and markdown files."""
        files = [
            f for f in Path("data/raw").rglob("*")
            if f.suffix in {".py", ".md"}
        ]

    def execute(self) -> None:
        if not self._is_valid("max_chunk_size", int):
            return
        self._load_corpus()
        self._init_splitters()
