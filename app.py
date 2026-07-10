"""
🎤 Offline AI Voice Assistant — Streamlit UI
Stack: Whisper (STT) + Ollama (LLM) + Piper (TTS)
"""

import streamlit as st
try:
    from model import whisper_model
    from model import piper
    import real_time_audio
    import LLM
    BACKEND_READY = True
except ImportError:
    BACKEND_READY = False


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Voice Assistant",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle at top, #1b1f3b 0%, #0e1024 60%, #090a1a 100%);
    }

    .hero {
        text-align: center;
        padding: 2.2rem 1rem 1.2rem 1rem;
    }
    .hero h1 {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #8ab4ff, #b39cff 40%, #ff9cd0 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero p {
        color: #9aa1c9;
        font-size: 0.95rem;
        letter-spacing: 0.02em;
    }

    .status-pill {
        display: inline-block;
        padding: 0.25rem 0.9rem;
        border-radius: 999px;
        background: rgba(120, 200, 140, 0.12);
        color: #7ee2a0;
        font-size: 0.78rem;
        font-weight: 600;
        border: 1px solid rgba(126, 226, 160, 0.35);
        margin-top: 0.4rem;
    }
    .status-pill.offline {
        background: rgba(230, 160, 90, 0.12);
        color: #f0b46a;
        border: 1px solid rgba(240, 180, 106, 0.35);
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.045);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 1.3rem 1.4rem;
        backdrop-filter: blur(6px);
        height: 100%;
    }
    .glass-card h4 {
        margin-top: 0;
        color: #e6e8ff;
        font-size: 1.0rem;
        font-weight: 700;
    }
    .glass-card .body-text {
        color: #c9cbe8;
        font-size: 0.95rem;
        line-height: 1.55;
        white-space: pre-wrap;
    }
    .placeholder-text {
        color: #6b7099;
        font-style: italic;
        font-size: 0.9rem;
    }

    div.stButton > button {
        border-radius: 999px;
        border: none;
        background: linear-gradient(135deg, #6a7dff, #b56af0);
        color: white;
        font-weight: 700;
        padding: 0.75rem 1.4rem;
        font-size: 1.02rem;
        box-shadow: 0 6px 22px rgba(120, 100, 255, 0.35);
        transition: transform 0.15s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.01);
        color: white;
        border: none;
    }
    div.stButton > button:active {
        transform: translateY(0px) scale(0.99);
    }

    .chat-bubble-user, .chat-bubble-ai {
        border-radius: 16px;
        padding: 0.7rem 1rem;
        margin: 0.35rem 0;
        font-size: 0.92rem;
        line-height: 1.5;
        max-width: 90%;
    }
    .chat-bubble-user {
        background: rgba(106, 125, 255, 0.16);
        border: 1px solid rgba(106, 125, 255, 0.3);
        color: #dfe2ff;
        margin-left: auto;
        text-align: right;
    }
    .chat-bubble-ai {
        background: rgba(181, 106, 240, 0.12);
        border: 1px solid rgba(181, 106, 240, 0.28);
        color: #ecdfff;
    }

    .section-label {
        color: #8890c2;
        font-size: 0.78rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================
defaults = {"text": "", "answer": "", "audio": "", "history": []}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HERO HEADER
# ============================================================
pill_class = "status-pill" if BACKEND_READY else "status-pill offline"
pill_text = "🟢 Backend Connected" if BACKEND_READY else "🟠 Demo Mode — backend modules not found"

st.markdown(f"""
<div class="hero">
    <h1>🎤 Offline Voice Assistant</h1>
    <p>Whisper · Ollama · Piper — 100% local, no internet required</p>
    <span class="{pill_class}">{pill_text}</span>
</div>
""", unsafe_allow_html=True)

st.write("")

# ============================================================
# RECORD BUTTON (centered)
# ============================================================
_, center_col, _ = st.columns([1, 1.3, 1])
with center_col:
    ask_clicked = st.button("🎙️  Start Recording", use_container_width=True)

st.write("")

# ============================================================
# PROCESSING PIPELINE
# ============================================================
if ask_clicked:
    progress = st.progress(0)

    with st.status("🎤 Listening...", expanded=True) as status:

        # ---- Record ----
        if BACKEND_READY:
            input_audio = real_time_audio.rec_audio()
        progress.progress(20)
        status.write("✅ Recording captured")

        # ---- Whisper: speech → text ----
        status.write("📝 Transcribing with Whisper...")
        if BACKEND_READY:
            text = whisper_model.stt(input_audio)
        progress.progress(45)

        # ---- Ollama: generate response ----
        status.write("🤖 Thinking with Ollama...")
        if BACKEND_READY:
            answer = LLM.llm(text)
            
        progress.progress(75)

        # ---- Piper: text → speech ----
        status.write("🔊 Synthesizing voice with Piper...")
        if BACKEND_READY:
            output_audio = piper.tts(answer)
        progress.progress(100)

        status.update(label="✅ Completed", state="complete")

    # ---- Save to session state ----
    st.session_state.text = text
    st.session_state.answer = answer
    st.session_state.audio = output_audio
    st.session_state.history.append(
        {"user": text, "assistant": answer}
    )

st.write("")

# ============================================================
# TRANSCRIPT + AI RESPONSE
# ============================================================
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 📝 Transcript")
    if st.session_state.text:
        st.markdown(f'<div class="body-text">{st.session_state.text}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="placeholder-text">Your speech will appear here...</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 🤖 AI Response")
    if st.session_state.answer:
        st.markdown(f'<div class="body-text">{st.session_state.answer}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="placeholder-text">The assistant\'s reply will appear here...</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ============================================================
# AUDIO PLAYER
# ============================================================
if st.session_state.audio:
    st.markdown('<div class="section-label">🔊 Audio Response</div>', unsafe_allow_html=True)
    st.audio(st.session_state.audio)
    st.write("")

# ============================================================
# CONVERSATION HISTORY
# ============================================================
if st.session_state.history:
    with st.expander(f"📜 Conversation History ({len(st.session_state.history)})", expanded=False):
        for chat in reversed(st.session_state.history):
            st.markdown(f'<div class="chat-bubble-user">🙂 {chat["user"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-bubble-ai">🤖 {chat["assistant"]}</div>', unsafe_allow_html=True)
            
