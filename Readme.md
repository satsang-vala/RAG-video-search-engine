# 🎥RAG AI Assistant

A Retrieval-Augmented Generation (RAG) project that helps users find specific topics in course videos.

Simply ask a question, and the system retrieves relevant video transcripts and provides the video name, timestamp, and related content.

## 🚀 Features

- Video-to-audio conversion using FFmpeg.
- Audio transcription using OpenAI Whisper.
- Transcript chunking with timestamps.
- Embedding generation using BGE-M3.
- Semantic search using Cosine Similarity.
- Retrieves the top 3 relevant transcript chunks.
- Supports Local LLM and Cloud LLM inference.

## 🛠️ Tech Stack

- Python
- OpenAI Whisper
- Ollama
- BGE-M3
- Qwen2.5 (3B)
- Groq API
- Pandas, NumPy, Scikit-learn
- FFmpeg

## 📂 Project Files & Their Responsibilities

| File | Description |
|---|---|
| `video_to_mp3.py` | Converts course videos into MP3 audio files using FFmpeg. |
| `mp3_to_jsons.py` | Transcribes audio using Whisper and generates JSON files containing transcript segments and timestamps. |
| `merge_chunks.py` | Combines every 5 transcript segments into larger chunks. |
| `Create_embeddings.py` | Generates BGE-M3 embeddings for transcript chunks using Ollama and saves them in `embeddings.joblib`. |
| `incoming_querry_llm.py` | Retrieves relevant chunks and generates answers using the local Qwen2.5 LLM through Ollama. |
| `incoming_querry_llm_groq.py` | Uses the same retrieval process but generates answers using the cloud-based Groq API. |
| `requirements.txt` | Contains all required Python dependencies. |
| `.env` | Stores the Groq API key and configuration securely. |
| `README.md` | Contains project documentation and setup instructions. |

### Generated Files & Folders

| File / Folder | Purpose |
|---|---|
| `audios/` | Stores extracted audio files. |
| `jsons/` | Stores Whisper-generated transcript JSON files. |
| `newjsons/` | Stores merged transcript chunks. |
| `embeddings.joblib` | Stores transcript data and generated embeddings. |
| `prompt.txt` | Stores the prompt sent to the LLM. |
| `response.txt` | Stores the generated answer. |

## 🔄 How It Works

1. Convert course videos into audio files.
2. Transcribe audio using Whisper.
3. Combine transcript segments into chunks.
4. Generate embeddings using BGE-M3.
5. Store embeddings using Joblib.
6. Convert the user's question into an embedding.
7. Retrieve the top 3 relevant chunks using Cosine Similarity.
8. Send the retrieved context to an LLM.
9. Generate an answer containing the video name and timestamps.

## 🤖 Two LLM Methods

### 1. Local LLM – Ollama + Qwen2.5 (3B)

- Runs directly on your computer.
- Uses Qwen2.5 (3B) for answer generation.
- No LLM API key required.
- Uses your system's RAM and GPU resources.
- Supports local inference after downloading the model.

Download the model:

```bash
ollama pull qwen2.5:3b
```

Run:

```bash
python incoming_querry_llm.py
```

### 2. Cloud LLM – Groq API

- Uses Groq's cloud infrastructure for answer generation.
- Uses GPT-OSS 20B by default.
- Requires a Groq API key.
- No need to download the LLM locally.
- Requires an internet connection.

Install dependencies:

```bash
pip install groq python-dotenv
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Generate your API key:

https://console.groq.com/keys

Run:

```bash
python incoming_querry_llm_groq.py
```

**Note:** Both methods use Ollama + BGE-M3 for local embedding generation and semantic retrieval. Only the final LLM inference changes.

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd video-course-rag-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg and Ollama, then download the embedding model:

```bash
ollama pull bge-m3
```

For Local LLM inference, also download:

```bash
ollama pull qwen2.5:3b
```

## ▶️ Run the Project

Execute the scripts in the following order:

```bash
python video_to_mp3.py
python mp3_to_jsons.py
python merge_chunks.py
python Create_embeddings.py
```

Then choose your preferred LLM:

**Local LLM:**

```bash
python incoming_querry_llm.py
```

**Cloud LLM (Groq):**

```bash
python incoming_querry_llm_groq.py
```

## 📁 Project Structure

```text
video-course-rag-assistant/
│
├── Video/
├── audios/
├── jsons/
├── newjsons/
│
├── video_to_mp3.py
├── mp3_to_jsons.py
├── merge_chunks.py
├── Create_embeddings.py
├── incoming_querry_llm.py
├── incoming_querry_llm_groq.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔮 Future Improvements

- Build a web interface using Streamlit.
- Support more video formats.
- Improve timestamp accuracy.
- Integrate additional LLM providers.

## 👨‍💻 Author

**Satsang Vala**

GitHub: https://github.com/satsang-vala
Linkdin: www.linkedin.com/in/satsang-vala