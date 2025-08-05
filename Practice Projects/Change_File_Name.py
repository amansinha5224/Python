import os

def changeFileName(dir, exe):
    count = 1
    for file in os.listdir(dir):
        if(file.endswith(exe)):
            oldPath = os.path.join(dir, file)
            newPath = os.path.join(dir, str(count)+exe)
            os.rename(oldPath, newPath)
            count += 1
    
    print('DONE')
    
# 'C:/Users/user/Pictures/Saved Pictures/DEMO'
if __name__ == "__main__":
    path = input("Specify Path of The Folder/File: ")
    exe = input("Specify Extension (example '.exe'): ")

    changeFileName(path, exe)