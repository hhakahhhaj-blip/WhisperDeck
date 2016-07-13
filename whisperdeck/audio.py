"""Wav loading, trimming and simple DSP helpers (stdlib only)."""

import struct
import wave
from pathlib import Path


class AudioError(Exception):
