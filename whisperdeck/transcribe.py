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


def transcribe_file(wav_path, model="base.en", language="auto", threads=4):
    """Run whisper.cpp on a wav and return plain text."""
    binary = find_binary()
    model_path = Path("models") / f"ggml-{model}.bin"
    if not model_path.exists():
