import os
import shutil
def remove_online(osudir):
    bgdir = os.path.join(osudir, r"Data\bg")
    for image in os.scandir(bgdir):
        shutil.copy2(r"StockImage1.png", os.path.join(bgdir, image.name))