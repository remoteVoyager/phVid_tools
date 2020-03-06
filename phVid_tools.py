import exifread, re, os, sys, glob, time, csv, cv2
from pathlib import Path


####################################################################################
# snakeye's https://gist.github.com/snakeye/fdc372dbf11370fe29eb gist
####################################################################################

def _get_if_exist(data, key):
    if key in data:
        return data[key]

    return None


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

    
def get_exif_location(exif_data):
    """
    Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
    """
    lat = None
    lon = None

    gps_latitude = _get_if_exist(exif_data, 'GPS GPSLatitude')
    gps_latitude_ref = _get_if_exist(exif_data, 'GPS GPSLatitudeRef')
    gps_longitude = _get_if_exist(exif_data, 'GPS GPSLongitude')
    gps_longitude_ref = _get_if_exist(exif_data, 'GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref.values[0] != 'N':
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref.values[0] != 'E':
            lon = 0 - lon

    return lat, lon

####################################################################################
# end of snakeye's gist
####################################################################################


def get_exif_data(image_file):
    with open(image_file, 'rb') as f:
        exif_tags = exifread.process_file(f)
        
    return exif_tags 


def get_img_gps(image_file):
    lat, lon = get_exif_location(get_exif_data(image_file))
    lat = round(lat, 6)
    lon = round(lon, 6)

    return [lat, lon]


def get_img_param(image_file, key):
    data = get_exif_data(image_file)

    return(_get_if_exist(data, key))


def get_img_dir_gps(dir=None, verbose = False):
    
    if dir is None:
        dir='*'

    dir += '.JPG'

    imgs = glob.glob(dir)

    imgs_gps = []

    for img in imgs:
        imgs_gps.append([img, time.ctime(os.path.getmtime(img))] + get_img_gps(img))
    
    if verbose:
        print(imgs_gps)
    
    return imgs_gps

def get_img_dir_gps_csv(dir=None):

    imgs_gps = get_img_dir_gps(dir)

    header = ['file_path', 'date', 'latitude', 'longitude']

    out_path = 'out.csv'
    i = 1

    while os.path.exists(out_path):
        out_path = 'out_{}.csv'.format(i)
        i+=1


    with open(out_path, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)     # write header row
        writer.writerows(imgs_gps)  # write records
    

# TODO: extract frame from photo
    
def extract_frame(vid_src, frame_no):

    current_frame = 0

    vid = cv2.VideoCapture(vid_src)

    out_frame = None
    
    succes = True

    while succes and current_frame<frame_no:

        succes, frame = vid.read()

        current_frame += 1

        out_frame = frame_no

    # generate name for frame image:
    path = os.path.basename(vid_src).split('.')[0] + '.JPG'

    # write image
    cv2.imwrite(path, frame)

    vid.release()
    cv2.destroyAllWindows()

    return path


    

            









