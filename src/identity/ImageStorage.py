from PIL import Image
##
# This class implements storage of image data for display as a QPixmap
class ImageStorage(object):
    def __init__(self, path):
        image = Image.open(path)
        self.data = dict(data=image.tobytes(),
                         size=image.size,
                         mode=image.mode)

    ##
    # Returns the image represented by this instance as a PIL.Image object
    # You can then call toqpixmap() on this object
    def get_repr(self):
        return Image.frombytes(self.data['mode'], self.data['size'], self.data['data'])