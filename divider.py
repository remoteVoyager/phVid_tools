# skrypt do rodzielania plików z misji smogowej na foldery zawierające poszczególne kominy (na bazie danych z exif)

import phVid_gps_tools as phvid
import os, sys, glob
from datetime import datetime, timedelta, date
from pathlib import Path
import shutil

# TODO: podziel 

def divide(cycles=None):

    subpath = ''

    mp4s = glob.glob( subpath + '*.MP4')
    jpgs = glob.glob( subpath + '*.JPG')

    files = mp4s + jpgs
    files = files.sort(key=os.path.getmtime)

    i = 0

    while i<len(files):

        img_path = files[i+2]

        # get time for folder name
        img_time = datetime.strptime(phvid.get_img_param(img_path, 'Image DateTime'), '%Y:%m:%d %H:%M:%S')

        # dir_path = Path(__file__).resolve().parent / img_time.strftime('%Y%m%d_%H%M')

        # try:
        #     dir_path.mkdir()
        # except FileExistsError:
        #     dir_path = Path(__file__).resolve().parent / img_time.strftime('%Y%m%d_%H%M') + '_2'

        for j in range(4):
            #shutil.copy2(files[i+j], dir_path)
            print('i={} file={}'.format(i, files[j]))
        i+=4
        
