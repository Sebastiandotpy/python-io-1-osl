import os

DATA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "data", "initial")

def create_data_directories(directory_list):
    for directory in directory_list:
        dir_path = os.path.join(DATA_ROOT, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {directory}")
        else:
            print(f"The directory {directory} already exists.")

dirs = ["personal", "work"]


create_data_directories(dirs)
