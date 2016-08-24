"""Energy-based voice activity detection for pre-trim."""

from .audio import rms_levels


def speech_windows(path, threshold=0.04, pad_s=0.4):
    """Return [(start_s, end_s)] spans above the RMS threshold."""
    levels = rms_levels(path, window_s=0.25)
