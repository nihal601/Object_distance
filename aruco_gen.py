import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
# %matplotlib nbagg

# aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)

fig = plt.figure()
nx = 1
ny = 1
for j in range(1,5):
    for i in range(1, nx*ny+1):
        ax = fig.add_subplot(ny,nx, i)
        img = aruco.drawMarker(aruco_dict,j,100)
        plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
        ax.axis("off")

    plt.savefig("ID_{}.pdf".format(j))
    print(j)
    # plt.show()
    