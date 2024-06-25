import os

path = "/path/to/folder"
name = "file.txt"

fullname = os.path.join(path, name)
print(fullname)  # Output: /path/to/folder/file.txt
