from abc import ABC, abstractmethod


class PipelineStep(ABC):
    """Abstract class to define pipeline steps."""

    @abstractmethod
    def execute(self) -> None:
        """Execute a single step of the pipeline."""
        ...

    @abstractmethod
    def execute_dataset(self, path1: str, path2: str) -> None:
        """Execute a pipeline step over a whole dataset."""
        ...
