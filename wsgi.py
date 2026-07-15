import os
import sys

# Pass dummy args to make libretranslate.main() parse correctly
sys.argv = ["libretranslate"]

# Run main with explicit defaults via env vars
os.environ.setdefault("LT_DISABLE_WEB_UI", "false")

from libretranslate.main import main

# main() returns the Flask app instance
app = main()
