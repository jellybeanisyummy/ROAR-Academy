from matplotlib import pyplot
from matplotlib import image
import os

# load the original Lenna image
current_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_path, '..', 'samples')      # '..' in order to go up one directory
original_lenna = image.imread(path + '/lenna.bmp')

''' Alternative way to load the image using pathlib:
from pathlib import Path
from matplotlib import image

# Get current file's directory
current_path = Path(__file__).parent

# Navigate to the file
image_path = current_path / '..' / 'images' / 'lenna.bmp'
# Or: image_path = current_path.parent / 'images' / 'lenna.bmp'

original_image = image.imread(str(image_path))
'''
pyplot.subplot(1, 2, 1)
pyplot.imshow(original_lenna)

# get flag image
flag = image.imread(current_path + '/taiwan-flag-xs.png')
row, col = flag.shape[:2]

print(f"Lenna dtype: {original_lenna.dtype}")  # Might be uint8 (0-255)
print(f"Flag dtype: {flag.dtype}")             # Might be float32 (0.0-1.0)

# convert flag from float32 to uint8
flag = (flag * 255).astype('uint8')

# create modified lenna image with flag overlay
modified_lenna = original_lenna.copy()
# These images might have different data types:
modified_lenna[:row, :col] = flag
pyplot.subplot(1, 2, 2)
pyplot.imshow(modified_lenna)
pyplot.show()