import matplotlib.pyplot as plt
import numpy as np
from antennasAndArrays import AntennaArray

ar = AntennaArray([[0,0,0],[0,1,0], [1,0,0], [1,1,0]], [1,2,3,4])

angles = np.linspace(0, 1, num=3)
radPat = ar.arrayFactor([0,1,2,4,5,6], [0,1,2,3,4])
print(radPat)
#plt.imshow(radPat)