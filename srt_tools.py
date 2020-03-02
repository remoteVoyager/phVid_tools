# useful functions for SRT (subtitle) files

import re, os, glob

def get_gps_list(src, frame_rate=None):
    """ get list of positions from SRT file (created for SRTs from DJI enterprise drones) 
    
    retruns list 
    
    """

    output = []
    frame = 0

    srt_file = open(src)

    for line in srt_file:
        
        # skip all lines without camera data.
        if line[0] != '[':
            continue
        else:
            # extract and strip regex matches
            lon= float((re.findall(r'latitude: \d*.\d*', line)[0]).split(' ')[1])
            lat= float((re.findall(r'longtitude: \d*.\d*', line)[0]).split(' ')[1])

            frame += 1

            # store
            if frame_rate:
                time = frame * 1.0 / frame_rate 
                output.append((frame, time, round(lon, 6), round(lat, 6)))
            else:
                output.append((round(lon, 6), round(lat, 6)))

    return output

def get_avg_gps(src):
    """ calculate avg gps position from SRT file """
    
    pos_list = get_gps_list(src)

    lat_sum = sum(lat for lat, lon in pos_list)
    lon_sum = sum(lon for lat, lon in pos_list)

    lat_avg = round(lat_sum / len(pos_list),6)
    lon_avg = round(lon_sum / len(pos_list),6)

    return lat_avg, lon_avg


def get_dir_avg_gps(dir = None):
    
    if dir is None:
        dir = '*'
    
    dir += '.SRT'

    files = glob.glob(dir)

    out_list = []

    for f in files:
        out_list.append((f,) + get_avg_gps(f))

    return out_list