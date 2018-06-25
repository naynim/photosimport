import glob, os, shutil, subprocess

name_of_file = "input name of file"
source_path = r"input source file address"
file_list = os.listdir(source_path)
newpath = r'input new path, must not be created'
raw_folder = (newpath + r"\RAW")
jpg_folder = (newpath + r"\JPG")
vid_folder = (newpath + r"\VID")
def import_flow():
#(1)create directory
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    print(newpath + " created")
#(2)create subfolders (raw/jpg/vid)
    if not os.path.exists(raw_folder):
        os.makedirs(raw_folder)
    if not os.path.exists(jpg_folder):
        os.makedirs(jpg_folder)
    if not os.path.exists(vid_folder):
        os.makedirs(vid_folder)
    print("raw, jpg, vid folders created")
#(3)separate file types into various folders
    files = glob.iglob(os.path.join(source_path, "*.raf"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, raw_folder)
    print("raw files copied")
    files = glob.iglob(os.path.join(source_path, "*.jpg"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, jpg_folder)
    print("jpg files copied")
    files = glob.iglob(os.path.join(source_path, "*.MP4"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, vid_folder)
    print("video files copied")
    files = glob.iglob(os.path.join(source_path, "*.MOV"))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, vid_folder)
    print("mov files copied")
    print("all files copied... beginning to rename")
#(4)rename file type in consecutive no. order
    raw_files = os.listdir(raw_folder)
    print(raw_files)
    saved_path = os.getcwd()
    print("current working directory is " + saved_path)
    os.chdir(raw_folder)
    i = 1
    for file_name in raw_files:
        print("Old Name - " + file_name)
        print("New Name - " + name_of_file + str(i)+".RAF")
        os.rename(file_name, name_of_file + str(i)+".RAF")
        i = i+1
    print("All raw files renamed")
    jpg_files = os.listdir(jpg_folder)
    print(jpg_files)
    saved_path = os.getcwd()
    print("current working directory is " + saved_path)
    j = 1
    os.chdir(jpg_folder)
    for file_name in jpg_files:
        print("Old Name - " + file_name)
        print("New Name - " + name_of_file + str(j)+".jpg")
        os.rename(file_name, name_of_file + str(j)+".jpg")
        j = j + 1
    print("All jpg files renamed")
    vid_files = os.listdir(vid_folder)
    print(vid_files)
    saved_path = os.getcwd()
    print("current working directory is " + saved_path)
    k = 1
    os.chdir(vid_folder)
    for file_name in vid_files:
        print("Old Name - " + file_name)
        print("New Name - " + name_of_file + str(k)+".mov")
        os.rename(file_name, name_of_file + str(k)+".mov")
        k = k + 1
    print("All videos renamed")
#(5)counting number of files for each type
    list_jpg = os.listdir(jpg_folder)
    list_raw = os.listdir(raw_folder)
    list_vid = os.listdir(vid_folder)
    total_jpg = len(list_jpg)
    total_raw = len(list_raw)
    total_vid = len(list_vid)
    print("total number of raw files: "+str(total_raw))
    print("total number of jpg files: "+str(total_jpg))
    print("total number of video files: "+str(total_vid))

#(6)open lightroom
    print("opening lightroom...")
    subprocess.Popen(["C:\Program Files\Adobe\Adobe Lightroom\Lightroom.exe"])

import_flow()



    
