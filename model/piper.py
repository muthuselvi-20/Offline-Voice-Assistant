import subprocess
from playsound import playsound
import os
from datetime import datetime

model = r"D:\Projects\AI Voice Assistant\model\Piper-model\en_US-lessac-medium.onnx"
conf = r"D:\Projects\AI Voice Assistant\model\Piper-model\en_US-lessac-medium.onnx.json"
piper = r"D:\Projects\AI Voice Assistant\.venv\Scripts\piper.exe"

os.makedirs("output",exist_ok=True)

def tts(text):
    output_file = os.path.join(r"D:\Projects\AI Voice Assistant\output",datetime.now().strftime("speech_%Y%m%d_%H%M%S.wav"))
    subprocess.run([
    piper,
    "-m",model,
    "-c",conf,
    "--text",text,
    "-f",output_file
    ])
    print("Audio stored...")
    return output_file

