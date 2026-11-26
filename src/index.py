import bm25s
from tqdm import tqdm
from pathlib import Path
from .file import File
from .pipeline_step import PipelineStep

from chonkie import (
    Chunk,
    CodeChunker,
    RecursiveChunker,
    RecursiveRules,
    RecursiveLevel
)


class Index(PipelineStep):
    """Loads the corpus to split it into chunks and indexes them."""

    md_rules = RecursiveRules(
        levels=[
            RecursiveLevel(
                delimiters=[
                    "\n# ", "\n## ", "\n### ",
                    "\n#### ", "\n##### ", "\n###### "
                ],
                include_delim="next"
            ),
            RecursiveLevel(delimiters=["\n\n"]),
            RecursiveLevel(delimiters=["\n"]),
            RecursiveLevel(
                delimiters=[". ", "! ", "? "],
                include_delim="prev"
            ),
            RecursiveLevel(whitespace=True),
        ]
    )

    def __init__(self, max_chunk_size: int) -> None:
        """Initialize the index class."""
        self.max_chunk_size = max_chunk_size

    def _load_corpus(self) -> list[Path]:
        """Load all the python and markdown files."""
        files = [
            f for f in Path("data/raw").rglob("*")
            if f.suffix in {".py", ".md"}
        ]
        return files

    def _store_chunks(
        self, chunks: list[Chunk], file: Path
    ) -> list[dict[str, str | int]]:
        """Store the chunks into a list."""
        stored_chunks = []

        for chunk in chunks:
            stored_chunks.append({
                "text": chunk.text,
                "file_path": str(file),
                "file_type": file.suffix,
                "start_index": chunk.start_index,
                "end_index": chunk.end_index,
            })
        return stored_chunks

    def _create_chunks(self, files: list[Path]) -> None:
        """Split the files to create the chunks."""
        py_chunker = CodeChunker(
            language="python", chunk_size=self.max_chunk_size
        )

        md_chunker = RecursiveChunker(
            rules=self.md_rules, chunk_size=self.max_chunk_size
        )

        stored_chunks = []

        for file in tqdm(files, desc="Chunking", unit="file"):
            chunker = py_chunker if file.suffix == ".py" else md_chunker
            chunks = chunker.chunk(file.read_text())

            stored_chunks.extend(self._store_chunks(chunks, file))

    def execute(self) -> None:
        if not self._is_valid("max_chunk_size", int):
            return
        files = self._load_corpus()
        self._create_chunks(files)
