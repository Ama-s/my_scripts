import os

def automate_task(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)

    # Print the list of files
    print("Files in the folder:")
    for file in files:
        print(file)

# Example usage
folder_path = r"C:\Users\user\Downloads"
automate_task(folder_path)
