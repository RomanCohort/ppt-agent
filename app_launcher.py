import os
import sys

from streamlit.web import cli as stcli


def _resolve_app_path() -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "streamlit.py")
    return os.path.join(os.path.dirname(__file__), "streamlit.py")


def main() -> int:
    app_path = _resolve_app_path()
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
    ]
    return stcli.main()


if __name__ == "__main__":
    raise SystemExit(main())
