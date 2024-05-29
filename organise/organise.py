import os #to talk to my computer 
import time #a package to keep track of the time
from watchdog.observers import Observer                 #the watch package is to watch out for new files
from watchdog.events import FileSystemEventHandler

class DesktopHandler(FileSystemEventHandler):
    def on_created(self, event):                    #Each time a new file pops up, DesktopHandler gets a special "created" event.
        if not event.is_directory:                  # If it's not a folder (because folders are already organized), it starts organizing!
            self.organize_file(event.src_path)

    def organize_file(self, file_path):
        file_name = os.path.basename(file_path)
        file_type = self.get_file_type(file_name)
        target_folder = self.get_target_folder(file_type)

        if target_folder:
            target_path = os.path.join(target_folder, file_name)
            os.rename(file_path, target_path)
            print(f"Moved {file_name} to {target_folder}")

    def get_file_type(self, file_name):
        _, file_extension = os.path.splitext(file_name)
        return file_extension.lower()
    
    def get_target_folder(self, file_type):
        folder_mapping = {
            ".pdf": "Documents",
            ".docx": "Documents",
            ".txt": "Documents",
            ".jpg": "Pictures",
            ".jpeg": "Pictures",
            ".png": "Pictures",
        }
        return folder_mapping.get(file_type, None)
if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Downloads")
    event_handler = DesktopHandler()
    observer = Observer()
    observer.schedule(event_handler, path=desktop_path, recursive=False)
    observer.start()

    try:
        print("Monitoring desktop for new files. Press Ctrl+C to exit.")
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
