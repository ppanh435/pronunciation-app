from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.transcribe import transcribe_audio
import traceback

router = APIRouter()


@router.post("/analyze")
async def analyze_pronunciation(
    audio: UploadFile = File(...),
    passage_id: str = Form(...),
    passage_text: str = Form(...),
    passage_title: str = Form(default=""),
):
    try:
        audio_bytes = await audio.read()
        if len(audio_bytes) < 100:
            raise HTTPException(status_code=400, detail="Audio too small")

        transcript = await transcribe_audio(audio_bytes, "audio/mpeg")

        return {
            "received": True,
            "filename": audio.filename,
            "size": len(audio_bytes),
            "transcript": transcript,
            "passage_id": passage_id,
        }
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))