import os
def remove_backgrounds(osudir):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    songdir = os.path.join(osudir, "Songs")
    for song in os.scandir(songdir):
        image_files = [
            item.path for item in os.scandir(song.path)
            if item.is_file() and os.path.splitext(item.name)[1].lower() in image_extensions
        ]
        for image in image_files:
            os.remove(image)
            