import os 
import sys 

def list_of_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None , f"{folder} does not exist"
    
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 sys.argv[0] <folder1> <folder2>..")
        sys.exit(1)
    
    folders=sys.argv[1:]
    for folder in folders:
        files = list_of_files_in_folder(folder)
        if files:
            print(f"\nlist of files from {folder}:-")
            for file in files:
                print(file)
        else:
            print(f"{folder} does not exist")
        
main()