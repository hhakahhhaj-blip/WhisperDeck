"""Registry/binary lookup without running whisper itself."""

import pytest

from whisperdeck.transcribe import TranscribeError, find_binary, transcribe_file
from whisperdeck.models import REGISTRY, suggest_model


