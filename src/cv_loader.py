import os
import pandas as pd


def load_resumes(data_dir="../data"):
    """
    Loads all .txt resume files from the specified directory into a dictionary.

    Args:
        data_dir (str): Path to the directory containing .txt resume files.

    Returns:
        dict: A dictionary where keys are filenames (without .txt) and values are the file contents as strings.
    """
    resumes = {}
    data_path = os.path.join(os.path.dirname(__file__), data_dir)

    if not os.path.exists(data_path):
        return resumes

    for filename in os.listdir(data_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_path, filename)
            key = os.path.splitext(filename)[0]
            with open(file_path, "r", encoding="utf-8") as f:
                resumes[key] = f.read()

    return resumes
