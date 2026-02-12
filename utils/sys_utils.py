import os

def get_file_path(file_name: str, caller_file: str):
    file_path = os.path.join(os.path.dirname(os.path.abspath(caller_file)), file_name)
    return file_path
