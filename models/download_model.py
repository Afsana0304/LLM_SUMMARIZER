import os
from huggingface_hub import snapshot_download

MODEL_DIR = os.path.join(os.path.dirname(__file__), "flan-t5-base-local")

if not os.path.exists(MODEL_DIR):
    print("⬇️  Downloading FLAN-T5-Base model to", MODEL_DIR)
    snapshot_download(
    repo_id="google/flan-t5-base",
    local_dir="flan-t5-base-local",
    local_dir_use_symlinks=False
)
    print("✅ Model download complete.")
else:
    print("✅ Model already downloaded at", MODEL_DIR)
