"""Tag sidecar round-trip."""

from whisperdeck.tags import read_tags, write_tags, add_tag, filter_by_tag


def test_roundtrip(tmp_path):
    p = tmp_path / "memo.wav"
