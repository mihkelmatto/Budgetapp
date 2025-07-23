from pathlib import Path

def root_directory(*parts) -> str:
    path = Path(__file__).resolve().parent.parent.joinpath(*parts)
    return str(path)