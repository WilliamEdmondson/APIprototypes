import sys
import dicom
import numpy as np
import pandas as pan

dm = dicom.read_file('sample.dcm')
print(dm.pixel_array) sys
sys.stdout.flush()
