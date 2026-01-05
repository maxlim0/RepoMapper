"""Public package interface for RepoMapper."""

from importlib.metadata import PackageNotFoundError, version

from .repomap import RepoMap

__all__ = ["RepoMap"]

try:
    __version__ = version("repomapper")
except PackageNotFoundError:  # pragma: no cover - not installed
    __version__ = "0.0.0"
