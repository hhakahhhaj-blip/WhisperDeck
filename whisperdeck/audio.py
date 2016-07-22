"""Wav loading, trimming and simple DSP helpers (stdlib only)."""

import struct
import wave
from pathlib import Path


class AudioError(Exception):
    pass


def load_wav(path):
    """Return (sample_rate, channels, frames_as_list_of_ints)."""
    p = Path(path)
    if not p.exists():
