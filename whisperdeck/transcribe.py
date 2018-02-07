"""Thin, honest wrapper around a local whisper.cpp binary."""

import shutil
import subprocess
from pathlib import Path


class TranscribeError(Exception):
    pass


def find_binary():
    for name in ("whisper-cli", "main", "whisper"):
        path = shutil.which(name)
        if path:
            return path
    raise TranscribeError(
        "whisper.cpp binary not found on PATH "
        "(see docs/model-zoo.md for build instructions)")


