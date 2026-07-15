import os
import sys

sys.argv = ["libretranslate", "--wsgi"]

# Optional: pass env vars as CLI args
env_mappings = {
    "LT_HOST": "--host",
    "LT_PORT": "--port",
    "LT_LOAD_ONLY": "--load-only",
    "LT_DISABLE_WEB_UI": "--disable-web-ui",
    "LT_API_KEYS": "--api-keys",
    "LT_REQ_LIMIT": "--req-limit",
    "LT_CHAR_LIMIT": "--char-limit",
}

for env_var, cli_arg in env_mappings.items():
    if env_var in os.environ:
        sys.argv.append(cli_arg)
        sys.argv.append(os.environ[env_var])

from libretranslate import main
app = main()
