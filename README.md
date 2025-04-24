# stem_ripper
Takes .mp3/.wav files and turns them into 4-model stems from DEMUCS.

A lightweight Python script that wraps DEMUCS stem separation tool. Automatically separates bass, drums, vocals, and other (instrumentation) stems from an input audio file using GPU acceleration (CUDA).

### Languages and styles used
<p>
    <a href="https://www.python.org/"><img height="28" width="28" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png" /></a>
</p>

## Screenshots
<img width=60% src="https://raw.githubusercontent.com/cameronos/stem_ripper/refs/heads/main/stem_sc.png">

## Features
- GPU-accelerated stem splitting via CUDA (if available)
- Timer for process duration

## Usage
To use the script, you need:
- Python 3.x
- Installed demucs and preferably mdx_extra or htdemucs model.
- Termcolor for terminal colors

To install dependencies, you can use pip:

```bash
pip install termcolor
pip install demucs

