"""The deck: ordered list of recordings with metadata."""

import time
from pathlib import Path

AUDIO_EXTS = {".wav", ".mp3", ".m4a", ".flac"}


class DeckItem:
    def __init__(self, path, mtime=None):
        self.path = Path(path)
