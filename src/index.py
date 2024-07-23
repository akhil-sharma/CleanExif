from PIL import Image as PillowImage
from exif import Image as ExifImage
from PIL import ExifTags
from os import listdir
from os.path import isfile, join



# Get a list of all the files from the specified location
# with an accepted file extension.
def getFileList(location: str, extensions: list[str] = ["jpg"]) -> list[str]:
    files = []
    for item in listdir(location):
        file_path = join(location, item)
        if isfile(file_path) and item.split(".")[-1] in extensions:
            files.append(file_path)
    return files

image_files = getFileList(location="../python_meta_dataset", extensions=["jpg"])

PILLOW_TAGS = [
    306,  # Date/Time Photo Taken
]

EXIF_TAGS = [
    "datetime_original",
]

for file in image_files:
    pillow_image = PillowImage.open(file)
    img_exif = pillow_image.getexif()
    for tag in PILLOW_TAGS:
        try:
            img_exif[tag] = "2024:07:23 06:00:08"
            output_file = file[0: file.rfind(".")] + "_clrd_" + file[file.rfind("."):]
            pillow_image.save(output_file, exif=img_exif)
            print(f"Cleared file: {file}")
        except Exception as e:
            print(e)
            print(f" << Could not clear file: {file} >>")
            continue
