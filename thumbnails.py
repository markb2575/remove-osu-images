import os
import shutil
def remove_thumbnails(osudir):
    btdir = os.path.join(osudir, r"Data\bt")
    for image in os.scandir(btdir):
        shutil.copy2(r"StockImage2.png", os.path.join(btdir, image.name))