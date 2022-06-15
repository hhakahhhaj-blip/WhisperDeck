"""VAD window sanity on a synthetic clip."""

import struct, wave

from whisperdeck.vad import speech_windows, total_speech_seconds


def _mk(path, rate=8000, secs=2.0, loud_until=1.0):
    n = int(rate * secs)
    frames = []
