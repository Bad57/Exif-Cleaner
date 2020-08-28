# Imports 
from PIL import Image, ExifTags
from shutil import copyfile

class Cleaner:

    # Constructor
    def __init__(self, path):
        self.path = path
        self.openFile()
        
    # Open Image file
    def openFile(self):
        if self.path != "":
            self.file = Image.open(self.path)

    # Get Exif Data from Image
    def getExifData(self):
        self.exif_data = self.file.getexif()
    
    # Display exctracted exif datas
    def displayExifData(self):
        self.getExifData()
        img_exif_dict = dict(self.exif_data)
        if len(img_exif_dict.items()) <= 0:
            return print("No Exif data !")
        else:
            for key, val in img_exif_dict.items():
                if key in ExifTags.TAGS:
                    print(f"{ExifTags.TAGS[key]}:{repr(val)}")
    
    # Create a copy of the Image and clear all the exif datas
    def clearExifData(self):
        image_data = list(self.file.getdata())
        image_without_exif = Image.new(self.file.mode,self.file.size)
        image_without_exif.putdata(image_data)
        image_without_exif.save(u"clean_{}".format(self.path))
        print("Exif data cleaned !")

