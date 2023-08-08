import os
import shutil


DATA_ROOT = r"C:\Users\black\Desktop\class-of-2023\introduction\python-2023\projects\io-3-osi-Sebastiandotpy\src\data\initial"

def classify(categories):
    for category, files in categories.items():
        category_dir = os.path.join(DATA_ROOT, category)
        os.makedirs(category_dir, exist_ok=True)
        
        for file in files:
            source_path = os.path.join(DATA_ROOT, file)
            destination_path = os.path.join(category_dir, file)
            
            if os.path.exists(source_path):
                shutil.move(source_path, destination_path)
                print(f"Moved '{file}' to '{category}' directory.")
            else:
                print(f"File '{file}' not found in the initial directory.")
    
if __name__ == "__main__":
    categories = {
        "personal": ["todos.txt", "bookmarks.txt"],
        "work": ["customers.csv", "jobs.csv"]
    }
    
    classify(categories)
