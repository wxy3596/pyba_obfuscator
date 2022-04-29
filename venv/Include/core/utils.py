import sys
import glob
import os

class Utils:
    def __init__(self):
        self.platform = sys.platform

    def Platform(self, getOS, getPathType):
        if getOS == True:
            if self.platform == "win32":
                return "win32"
            else:
                return "unix"
        elif getPathType == True:
            if self.platform == "win32":
                return 1;
            else:
                return 2;
        else:
            return 0;