
import os
from django.utils.deconstruct import deconstructible
import time
from datetime import date

@deconstructible
class RenameUploadedFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        thisDate = str(date.today()).replace("-", "")
        thisTime = str(time.time())[:10]
        updatedFilename = thisDate + thisTime

        # if self.location == 'product':
        #     updatedFilename = 'prod_' + updatedFilename

        return self.path % (updatedFilename, extension)
