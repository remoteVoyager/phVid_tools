# skrypt do rodzielania plików z misji smogowej na foldery zawierające poszczególne kominy (na bazie danych z exif)
import os, re, sys
from PIL import Image
import pathlib
from exif_gps import get_img_gps
from utils import *



def divide( src = None):
    
    # przejdź przez wszystkie pliki


    # na podstawie exifu stwierdź które pliki są z tego samego czasu
    # równocześnie podziel je na typy

    # wygeneruj strukturę
    # DD-MM-YYYY:
    #     YYMMDD_HH_MM_SS:
    
    
    
    
    pass




test = 'DJI_0126.JPG'

print(get_img_gps(test))