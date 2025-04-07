import os
import shutil

files = []
type_files = []
pc_username = os.getlogin()
path = rf"C:\Users\{pc_username}"
os.chdir(path)

downloads = path + "\Downloads"

try:
    os.mkdir("media")
    os.chdir("media")
    os.mkdir("photos")
    os.mkdir("videos")
except FileExistsError:
    pass
photo_script = path + "\media\photos"
video_script = path + r"\media\videos"

os.chdir(downloads)

if os.getcwd() == downloads:
    all_downloads_files = os.listdir(downloads)
    for file in all_downloads_files:
        try:
            index_type_file = file.index(".")
            type_files.append(file[index_type_file::])
            files.append(file)
        except ValueError:
            ...


for file in files:
    if (
        file.endswith(".jpg")
        or file.endswith(".jpeg")
        or file.endswith(".png")
        or file.endswith(".gif")
    ):
        shutil.copy(file, photo_script)
        print("photos copied successfully")

    if (
        file.endswith(".mp4")
        or file.endswith(".avi")
        or file.endswith(".mkv")
        or file.endswith(".webm")
    ):
        shutil.copy(file, video_script)
        print("videos copied successfully")
