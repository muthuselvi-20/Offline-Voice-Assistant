# 🎤 Offline AI Voice Assistant

An offline AI Voice Assistant that listens to your voice, converts it into text, generates an intelligent response using a local Large Language Model, and replies with natural-sounding speech.

The project is built entirely with **Whisper**, **Ollama (Qwen3)**, **Piper**, and **Streamlit**, allowing it to work without cloud-based AI APIs.

---

# ✨ Features

* 🎙️ Record voice from your microphone
* 📝 Speech-to-Text using Whisper
* 🤖 AI response generation using Ollama (Qwen3)
* 🔊 Text-to-Speech using Piper
* 💻 Fully offline execution
* 🌐 Interactive Streamlit interface
* 📊 Live processing status and progress bar
* 📜 View speech transcript
* 🤖 View AI-generated response
* ▶️ Play generated speech directly in the browser

---

# 🛠️ Tech Stack

### Programming Language

* Python 3.11

### AI Models

* Whisper
* Qwen3 (Ollama)
* Piper TTS

### Frameworks

* Streamlit

### Libraries

* whisper
* ollama
* sounddevice
* scipy
* numpy
* torch
* playsound (optional)

### Tools

* FFmpeg
* Ollama
* Piper

---

# 📁 Project Structure

```text
AI Voice Assistant/
│
├── app.py                     # Streamlit application
├── LLM.py                     # Ollama integration
├── real_time_audio.py         # Audio recording
│
├── model/
│   ├── Piper-models           # Piper ONNX models
│   ├── whisper_model.py       # Speech-to-Text
│   └── piper.py               # Text-to-Speech
│
├── input/                     # Recorded audio files
├── output/                    # Generated speech files
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/muthuselvi-20/Offline-Voice-Assistant.git
cd Offline-Voice-Assistant
```

---

## 2. Create a Virtual Environment

Using **uv**

```bash
uv venv --python 3.11
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
uv sync
```

---

# Install FFmpeg

Download FFmpeg and add its **bin** folder to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

---

# Install Ollama

Install Ollama and verify:

```bash
ollama --version
```

Download the model:

```bash
ollama pull qwen3
```

Verify:

```bash
ollama list
```

---

# Install Piper

Download:

* Voice model (`.onnx`)
* Voice configuration (`.onnx.json`)

Place them in the appropriate project folders.

Example:

```text
model/
    piper-model/
        en_US-lessac-medium.onnx
        en_US-lessac-medium.onnx.json

```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

# 🔄 Project Workflow

```text
User
 │
 ▼
🎤 Record Voice
 │
 ▼
Whisper
(Speech → Text)
 │
 ▼
Ollama (Qwen3)
(Text → AI Response)
 │
 ▼
Piper
(Text → Speech)
 │
 ▼
Generated Audio
 │
 ▼
Streamlit UI
```

---

# 🖥️ User Interface

The application provides:

* 🎤 Record button
* 📊 Processing progress bar
* 🟢 Live processing status
* 📝 Speech transcript
* 🤖 AI response
* 🔊 Audio playback

---

# 📂 Input & Output

### Input

Recorded microphone audio is saved in the **input** folder.

Example:

```text
input/
    audio_20260710_153025.wav
```

### Output

Generated speech is stored in the **output** folder.

Example:

```text
output/
    speech_20260710_153030.wav
```

---

# 📦 Main Components

## Whisper

Converts recorded speech into text.

## Ollama (Qwen3)

Generates an AI response from the transcript.

## Piper

Converts the AI response into natural-sounding speech.

## Streamlit

Provides the graphical user interface for interacting with the assistant.

---

# 🚀 Future Improvements

* 🌍 Multi-language speech recognition
* 🌍 Multi-language text-to-speech
* 🎙️ Continuous voice conversation
* 🧠 Conversation memory
* 📂 Chat with PDFs using RAG
* 🗂️ Conversation history
* 🎨 Improved UI with animations
* ☁️ Cloud deployment option

---

# 👩‍💻 Author

**Muthuselvi A**

B.E. Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Passionate about Artificial Intelligence, Machine Learning, Deep learning and  Large Language Models

---

# 📄 License

This project is intended for educational, learning, and portfolio purposes.

 
