import json


def load_documents(file_path: str = "./data/docs.json"):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        raise
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
    raise
