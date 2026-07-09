import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from datetime import datetime

os.makedirs("input",exist_ok=True)

def rec_audio():
    fs = 16000
    print("Recording...")
    record = sd.rec(
        int(5*fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    file_name = os.path.join("D:/Projects/AI Voice Assistant/input",
                             datetime.now().strftime("audio_%Y%m%d_%H%M%S.wav"))
    print("Processing...")
    write(file_name,fs,record)

    return file_name


