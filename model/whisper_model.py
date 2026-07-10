import whisper

model = whisper.load_model("tiny")

def stt(audio):
    result = model.transcribe(audio,fp16=False)
    print("Audio -> Text")
    return result["text"]

