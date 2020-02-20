# dodatkowy kod wspomagający divider.py
import re

def get_srt_pos(src):
    """ pobierz uśrednioną lokalizację M2e w trakcie rejestracji filmu z pliku SRT """
    
    lon = []
    lat = []

    srt_file = open(src)

    for line in srt_file:
        
        # pomijanie linii nie zawierających danych gps
        if line[0] != '[':
            continue
        else:
            # ekstrakcja i przycinanie tekstu pozycji gps
            lon_t = float((re.findall(r'latitude: \d*.\d*', line)[0]).split(' ')[1])
            lat_t = float((re.findall(r'longtitude: \d*.\d*', line)[0]).split(' ')[1])

            # przechowywanie
            lon.append(lon_t)
            lat.append(lat_t)

    avg_pos = (sum(lon)/len(lon), sum(lat)/len(lat))

    return(avg_pos)