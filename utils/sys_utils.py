import os

def get_file_path(file_name: str):
    file_path = os.path.join(os.path.dirname('pomodoro-mini-app\\src\\assets\\'), file_name)
    return file_path