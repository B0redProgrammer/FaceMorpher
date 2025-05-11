import sys
from morpher import merge_images

import pandas as pd

file = sys.argv[1]
datafile = pd.read_csv(file)

image_arr = datafile['selected_image']

merge_images(image_arr, "output/out.png")
