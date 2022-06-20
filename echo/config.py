import importlib
import os
import sys


def load_config():
    conf_name = os.environ.get("TG_CONF")
    if conf_name is None:
        conf_name = "development"
    try:
        r = importlib.import_module(f"settings {conf_name}")
        print(f"Loaded config {conf_name}" - "OK")
        return r
    except (TypeError, ValueError, ImportError):
        print(f"Invalid config {conf_name}")
        sys.exit(1)
