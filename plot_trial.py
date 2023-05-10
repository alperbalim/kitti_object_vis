import matplotlib.pyplot as plt
import cv2
#from xvfbwrapper import Xvfb
import time
import os
''' os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join('/home', 'plugins', 'platforms')
print(os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']) '''
time.sleep(5)
from kitti_object import kitti_object, show_lidar_with_depth, show_lidar_on_image, \
                         show_image_with_boxes, show_lidar_topview_with_boxes


from mayavi import mlab
#mlab.init_notebook('ipy') # do not use 'x3d' backend which leads to color missing

dataset = kitti_object('/media/alper/DATADRIVE2/KITTI2/', 'training')

data_idx = 10
objects = dataset.get_label_objects(data_idx)
pc_velo = dataset.get_lidar(data_idx)
calib = dataset.get_calibration(data_idx)
img = dataset.get_image(data_idx)
img_height, img_width, _ = img.shape

fig_3d = mlab.figure(bgcolor=(0, 0, 0), size=(800, 450))
show_lidar_with_depth(pc_velo, objects, calib, fig_3d, True, img_width, img_height)
fig_3d
mlab.show()



