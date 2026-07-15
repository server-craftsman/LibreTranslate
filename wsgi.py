import os
import sys

# Force host/port via CLI args
port = os.environ.get("PORT", "10000")
sys.argv = [
    "libretranslate",
    "--host", "0.0.0.0",
    "--port", str(os.environ.get("PORT", "10000")),
    "--load-only", "en,vi",
    "--disable-files-translation",
]

from libretranslate.main import main
app = main()
