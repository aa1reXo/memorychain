# 🧠 MemoryChain

**MemoryChain** is a prototype for visual voice memory. It allows users to:
- Upload audio files
- Transcribe them using Whisper
- Summarize with DeepSeek LLM via HuggingFace
- Store and visualize memories on an interactive timeline

## 🚀 Features
- 📤 Audio upload (.wav/.mp3)
- 🧠 Whisper-based transcription
- ✨ Summarization using DeepSeek via Hugging Face API
- 📊 Interactive timeline using Plotly

## 🛠 Requirements
```bash
pip install -r requirements.txt
```

## 🔑 API Keys
Set your Hugging Face API key as an environment variable:
```bash
export HUGGINGFACE_TOKEN=your-key-here
```

## ▶️ Run It
```bash
streamlit run app.py
```

## 📁 Folder Structure
```
memorychain/
├── app.py
├── transcriber.py
├── summarizer.py
├── memory_store.py
├── timeline_ui.py
├── requirements.txt
└── README.md
```

## 📸 Screenshots
![Demo](https://via.placeholder.com/600x300.png?text=MemoryChain+Demo+UI)

## 📄 License
MIT

# setup.sh
#!/bin/bash

# Setup Python venv and install deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "✅ Setup complete. Run with: streamlit run app.py"