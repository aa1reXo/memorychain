import whisper
import tempfile

def transcribe(audio_file):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name
    result = model.transcribe(tmp_path)
    return result["text"]