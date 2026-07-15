from libretranslate.main import main
from libretranslate.app import create_app

# Override create_app signature nếu cần
import libretranslate.main as lt_main
_original_create_app = lt_main.create_app

def patched_create_app(args=None):
    if args is None:
        # Create empty args
        class Args: pass
        args = Args()
    return _original_create_app(args)

lt_main.create_app = patched_create_app

# Now safe to call
app = lt_main.create_app()
