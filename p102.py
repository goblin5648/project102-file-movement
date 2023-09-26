import os
import shutil

#shifting or organizeing files
source='C:/Users/elven/OneDrive/Desktop/image'
destination='C:/Users/elven/Downloads'
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    if ext == '':
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Project_Files"
        path3 = destination + '/' + "project_Files" + '/' + i
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('creating and moving')
            shutil.move(path1,path3)