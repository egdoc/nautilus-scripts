#!/usr/bin/env python3
"""
Author: Egidio Docile
Organize selected pictures by their creation date, using the exif
DateTimeOriginal tag
"""

import datetime
import os

from PIL import Image

DATETIME_ORIGINAL=36867

def main():
    for path in os.getenv('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS','').splitlines():
        try:
            exif_data = Image.open(path)._getexif()
        except OSError:
            continue

        try:
            date = datetime.datetime.strptime(exif_data[DATETIME_ORIGINAL], '%Y:%m:%d %H:%M:%S')
            directory = os.path.join(date.strftime('%Y'), date.strftime('%B'))
        except (KeyError, ValueError, TypeError):
            directory = "unsorted"

        os.makedirs(directory, exist_ok=True)
        os.rename(path, os.path.join(directory, os.path.basename(path)))

if __name__ == '__main__':
    main()
