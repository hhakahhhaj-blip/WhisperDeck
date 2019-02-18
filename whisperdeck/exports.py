"""Export decks and segment lists to srt / vtt / markdown."""

from pathlib import Path


def _stamp_srt(t):
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = int(t % 60)
