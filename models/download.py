#!/usr/bin/env python3
"""Fetch a ggml whisper model into models/."""

import argparse
import sys
import urllib.request
from pathlib import Path

BASE = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main"
