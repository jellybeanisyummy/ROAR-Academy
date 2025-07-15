from matplotlib import pyplot
from matplotlib import image
import os

# load the original Lenna image
path = os.path.dirname(os.path.abspath(__file__))
original_image = image.imread(path + '/lenna.bmp')
