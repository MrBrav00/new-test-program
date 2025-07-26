import os

def get_files_in_folder(folder_path="models"):
    try:
        return [f for f in os.listdir(folder_path) if f.endswith(".onnx")]
    except FileNotFoundError:
        return []

def filter_models(file_list):
    return [f for f in file_list if not f.startswith(".")]

def get_model_path(name, folder="models"):
    return os.path.join(folder, name)
