import os

def show_data_list():
    directory = "io-3-osi-Sebastiandotpy\src\data\initial"
    
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")


show_data_list()
