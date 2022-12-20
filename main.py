
from PIL import Image
from PIL.ExifTags import TAGS
import os
import exif
import math
from pprint import pprint
mydir = os.getcwd() + "/imgs/"
print(f"Current directory: {mydir}")
arr = []
for pic in os.listdir(mydir):
    data_dict = {}
    img = Image.open(mydir + pic)
    exif_data = img._getexif()
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        data = exif_data.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode(errors="ignore")
        else:
            data_dict[tag] = data
    south = list(data_dict["GPSInfo"][2])
    west = list(data_dict["GPSInfo"][4])
    coords = str(int(math.trunc(float(south[0])))) + "deg " + str(int(math.trunc(float(south[1])))) + "' " + str((south[2])) + '" S, ' + str(int(math.trunc(float(west[0])))) + "deg " + str(int(math.trunc(float(west[1])))) + "' " + str(int(math.trunc(float(west[2])))) + '" W'

    #degrees, minutes, seconds to latitude and longitude
    lat = float(south[0]) + float(south[1])/60 + float(south[2])/3600
    lon = float(west[0]) + float(west[1])/60 + float(west[2])/3600
    print(lat, lon) 
    print(coords)