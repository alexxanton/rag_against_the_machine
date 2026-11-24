from typing import Any
from abc import ABC, abstractmethod


class PipelineStep(ABC):
    """Abstract class to define pipeline steps."""

    def _is_valid(self, name: str, type_to_validate: type) -> None:
        """Validate any type."""
        value = getattr(self, name)
        if not isinstance(value, type_to_validate):
            print(f"Invalid type for '{name}': Expected {type_to_validate.__name__}")
            return False
        return True

    @abstractmethod
    def execute(self) -> None:
        """Execute a single step of the pipeline."""
        ...

    @abstractmethod
    def execute_dataset(self, path1: str, path2: str) -> None:
        """Execute a pipeline step over a whole dataset."""
        ...
