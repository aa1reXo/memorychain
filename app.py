import streamlit as st
from transcriber import transcribe
from summarizer import summarize
from memory_store import save_memory, load_memories
from timeline_ui import render_timeline

st.set_page_config(page_title="MemoryChain", layout="wide")
st.title("🧠 MemoryChain – Voice to Timeline")

uploaded_audio = st.file_uploader("Upload a short audio clip (.wav or .mp3)", type=["wav", "mp3"])

if uploaded_audio:
    with st.spinner("Transcribing..."):
        transcript = transcribe(uploaded_audio)
    st.success("Transcription complete")
    st.text_area("Transcript", transcript, height=200)

    with st.spinner("Summarizing..."):
        summary = summarize(transcript)
    st.success("Summary created")
    st.text_area("Summary", summary, height=100)

    if st.button("📌 Save to MemoryChain"):
        save_memory(summary, transcript)
        st.success("Memory saved!")

st.markdown("---")
st.subheader("🗂 Memory Timeline")
memories = load_memories()
fig = render_timeline(memories)
st.plotly_chart(fig, use_container_width=True)
