class CLI:
    """Contains methods for the command line interface."""

    def index(self, max_chunk_size: int = 2000) -> None:
        """Ingest data/raw/ and build the index under data/processed/."""
        from .index import Index
        Index(max_chunk_size).execute()

    def search(self, query: str, k: int) -> None:
        """Return the top-k sources for a single query."""
        from .search import Search
        Search(k, query).execute()

    def search_dataset(
        self, dataset_path: str, k: int, save_directory: str
    ) -> None:
        """
        Run search over a whole dataset and
        write a StudentSearchResults JSON file.
        """
        from .search import Search
        Search(k).execute_dataset(dataset_path, save_directory)

    def answer(self, query: str, k: int) -> None:
        """Answer a single query using the retrieved context."""
        from .answer import Answer
        Answer(k, query).execute()

    def answer_dataset(
        self, student_search_results_path: str, save_directory: str
    ) -> None:
        """
        Generate answers for a dataset,
        producing a StudentSearchResultsAndAnswer JSON file.
        """
        from .answer import Answer
        Answer().execute_dataset(student_search_results_path, save_directory)

    def evaluate(
        self, student_search_results_path: str, dataset_path: str
    ) -> None:
        """
        Report your own recall@k against a ground-truth dataset,
        for your own testing."""
        pass
