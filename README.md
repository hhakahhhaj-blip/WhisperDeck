# WhisperDeck

![ci-python](https://github.com/FjgarciaMac/WhisperDeck/actions/workflows/ci-python.yml/badge.svg)
![license](https://img.shields.io/badge/license-MIT-blue.svg)
![python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![platform](https://img.shields.io/badge/platform-local-green.svg)

**On-device audio transcription toolkit** - a Python engine plus a small
Android demo app. Trim, tag, transcribe and export your recordings.
Everything runs locally: audio never leaves the machine.

## Why this exists

I record a lot of voice memos and wanted one tool that could trim them, tag
them, and turn them into searchable text without uploading anything to a
server. WhisperDeck is that tool: a *deck* of recordings, transcribed on
device with a local [whisper.cpp](https://github.com/ggerganov/whisper.cpp)
build.

## Features

| | |
|---|---|
| **Local-first** | one-time model download is the only network call, ever |
| **Trim + tag** | wav trimming, VAD-based speech windows, sidecar tags |
