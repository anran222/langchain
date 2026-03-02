"""Tests for CLI module."""

from langchain_app.cli import build_greeting


def test_build_greeting_default() -> None:
    """build_greeting should return a default greeting."""
    assert build_greeting() == "Hello, World!"


def test_build_greeting_with_name() -> None:
    """build_greeting should include provided name."""
    assert build_greeting("Codex") == "Hello, Codex!"
