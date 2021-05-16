import shutil
import os
import time
from datetime import datetime, timedelta

cwd = os.getcwd()
source = cwd + '/folderA/'
destination = cwd + '/folderB/'

filesA = os.listdir(source)
filesB = os.listdir(destination)
files_to_transfer = []
filesB_length = len(filesB)
timecheck = datetime.now() - timedelta(1)


for a in filesA:
    timestampA = os.path.getmtime(source+a)
    i = 0
    for b in filesB:
        i += 1
        timestampB = os.path.getmtime(destination+b)
        if a == b and timestampA != timestampB and datetime.strptime(time.ctime(timestampA), '%a %b %d %H:%M:%S %Y') > timecheck:
            shutil.move(os.path.join(source, a), os.path.join(destination, b))
            break
        elif a != b and i == filesB_length:
            shutil.move(os.path.join(source, a), os.path.join(destination, a))
        

