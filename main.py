from scanner.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path To The Image To Be Scanned")
args = vars(ap.parse_args())
