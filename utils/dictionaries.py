import json
from utils.filepath import root_directory

def read_dict() -> dict:
    filepath = root_directory("Resources", "dict.json")

    with open(filepath, "r") as file:
        # json.dump(dictionary, file, indent=4)
        content = json.load(file)
    return content

print(read_dict())

def save_dict(dictionary: dict) -> None:
    filepath = root_directory("Resources", "dict.json")
    with open(filepath, "w") as file:
        json.dump(dictionary, file, indent=4)

def create_ongoing_expenses(title: str, account: str = None,
                            leftover: float = 0.0, additions: float = 0.0,
                            budget: int = 0, used: float = 0.0, remaining: float = 0.0) -> dict:

    return {title: {}}

def income() -> dict:
    pass