import json
import os
from uuid import uuid4
from datetime import datetime

MEMORY_FILE = "data/memories.jsonl"
os.makedirs("data", exist_ok=True)

def save_memory(summary, transcript):
    memory = {
        "id": str(uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "summary": summary,
        "transcript": transcript
    }
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(memory) + "\n")

def load_memories():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return [json.loads(line) for line in f.readlines()]
