"""wd - the WhisperDeck command line interface."""

import argparse
import sys

from .audio import duration_seconds
from .tags import read_tags
from .deck import Deck
from .exports import export_deck


def main(argv=None):
    ap = argparse.ArgumentParser(prog="wd")
