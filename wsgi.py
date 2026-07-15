import os
import sys

# Force host/port via CLI args
port = os.environ.get("PORT", "10000")
sys.argv = [
    "libretranslate",
    "--host", "0.0.0.0",
    "--port", port,
    "--load-only", "en,vi",  # Optional: only load needed langs
    "--disable-files-translation",  # Save memory
]

from libretranslate.main import main
app = main()
