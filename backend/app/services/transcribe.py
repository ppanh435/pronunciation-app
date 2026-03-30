import os
import tempfile
from pydub import AudioSegment


async def convert_to_wav(audio_bytes: bytes, mime_type: str = "audio/webm") -> str:
    """Convert audio bytes to wav file, return path to wav file."""
    ext_map = {
        "audio/webm": "webm",
        "audio/mp4": "mp4",
        "audio/wav": "wav",
        "audio/ogg": "ogg",
        "audio/mpeg": "mp3",
    }
    ext = ext_map.get(mime_type, "webm")

    # Lưu file tạm
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    # Convert sang wav
    wav_path = tmp_path.replace(f".{ext}", ".wav")
    audio = AudioSegment.from_file(tmp_path, format=ext)
    audio.export(wav_path, format="wav")

    # Xóa file tạm gốc
    os.unlink(tmp_path)

    return wav_path


async def transcribe_audio(audio_bytes: bytes, mime_type: str = "audio/webm") -> str:
    """Placeholder — sẽ gọi Whisper API."""
    wav_path = await convert_to_wav(audio_bytes, mime_type)
    os.unlink(wav_path)
    return "placeholder transcript"