"""Basic wav helper tests (synthetic file, no assets needed)."""

import struct, wave

from whisperdeck.audio import load_wav, trim, rms_levels


def _mk(path, rate=8000, secs=1.0):
    n = int(rate * secs)
    frames = [int(8000 * ((i % 40) / 40 - 0.5)) for i in range(n)]
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
