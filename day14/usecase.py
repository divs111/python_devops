# import os

# folders = input("Enter folder names with spaces in between: ").split()
# #print(folders). -- this will give a list
# for folder in folders:
#     #print(folder)
#     try:
#         files = os.listdir(folder)
#     except FileNotFoundError:
#         print(f" this folder {folder} does not exist, please mention valid one")
#         continue
#     except PermissionError:
#         print(f"Access to this folder named {folder}")
#     print("List files from the folder name :" +folder)
#     for file in files:
#         print(file)

import os

def list_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None , f"{folder} does not exist"


def main():
    folders=input("Enter the folder name: ").split()
    for folder in folders:
        files, error_msg = list_files_in_folder(folder)
        if files:
            print(f"\nFiles from {folder}:-")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder}:{error_msg}")

main()
