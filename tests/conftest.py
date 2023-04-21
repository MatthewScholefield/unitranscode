from pathlib import Path
import tempfile
import wave

import pytest


@pytest.fixture(scope='function')
def temp_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


def write_silence_file(
    path: Path, seconds: float, sample_rate=48000, sample_width=2, channels=2
):
    with wave.open(str(path), 'wb') as wf:
        wf: wave.Wave_write
        wf.setparams(
            (channels, sample_width, sample_rate, 0, 'NONE', 'not compressed')
        )
        wf.writeframes(
            b'\0' * int(sample_rate * seconds * channels * sample_width)
        )
        wf.close()


@pytest.fixture
def example_20s_wav_file(temp_folder: Path):
    example_path = temp_folder.joinpath('example_20s_wav_file.wav')
    write_silence_file(example_path, 20.0)
    yield example_path
    example_path.unlink()
