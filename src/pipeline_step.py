from sys import stderr


class PipelineStep():
    """Abstract class to define pipeline steps."""

    def _is_valid(self, name: str, type_to_validate: type) -> bool:
        """Validate any type."""
        attr = getattr(self, name)

        if type_to_validate is str:
            if len(attr) == 0:
                print("Query must not be empty.", file=stderr)
                return False
            return True

        if not type(attr) is type_to_validate:
            print(
                f"Invalid type for `{name}`: "
                f"Expected `{type_to_validate.__name__}`, "
                f"got `{type(attr).__name__}` instead.",
                file=stderr
            )
            return False

        if type(attr) is int and attr <= 0:
            print(
                f"Invalid value for `{name}`: Must be bigger than 0.",
                file=stderr
            )
            return False

        return True

    def execute(self) -> None:
        """Execute a single step of the pipeline."""
        raise NotImplementedError

    def execute_dataset(self, path1: str, path2: str) -> None:
        """Execute a pipeline step over a whole dataset."""
        raise NotImplementedError
