"""wd - the WhisperDeck command line interface."""

import argparse
import sys

from .audio import duration_seconds
from .tags import read_tags
from .deck import Deck
from .exports import export_deck


def main(argv=None):
    ap = argparse.ArgumentParser(prog="wd")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_deck = sub.add_parser("deck", help="list recordings in a deck")
    p_deck.add_argument("--dir", default=".")
    p_deck.add_argument("--tag", default=None)
