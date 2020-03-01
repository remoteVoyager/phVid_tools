# useful functions for SRT (subtitle) files

import re

def get_gps_list(src, frame_rate=None):
    """ get list of positions from SRT file (created for SRTs from DJI enterprise drones) """

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
                output.append(frame, time, round(lon, 6), round(lat, 6))
            else:
                output.append(frame, round(lon, 6), round(lat, 6))

    return output