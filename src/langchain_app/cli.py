"""Command-line entrypoint for the project."""

from __future__ import annotations


def build_greeting(name: str = "World") -> str:
    """Build a greeting string.

    Args:
      name: Name to greet.

    Returns:
      A greeting sentence.
    """
    return f"Hello, {name}!"


def main() -> int:
    """Run the CLI application.

    Returns:
      Process exit code.
    """
    print(build_greeting())
    return 0
