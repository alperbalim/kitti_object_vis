
import time
import os
import PyQt5
import os
# demo for plotting
# ne comment
from kitti_object import kitti_object, show_lidar_with_depth, show_lidar_on_image, \
                         show_image_with_boxes, show_lidar_topview_with_boxes

import matplotlib.pyplot as plt
#import cv2
from mayavi import mlab
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.dirname(PyQt5.__file__) + "/Qt/plugins/platforms"

#os.environ['QT_QPA_PLATFORM'] = 'offscreen'
dataset = kitti_object('/media/alper/DATADRIVE2/KITTI2/', 'training')

data_idx = 10
objects = dataset.get_label_objects(data_idx)
pc_velo = dataset.get_lidar(data_idx)
calib = dataset.get_calibration(data_idx)
img = dataset.get_image(data_idx)
img_height, img_width, _ = img.shape
img_lidar = show_lidar_on_image(pc_velo[:, :3], img, calib, img_width, img_height)
fig_3d = mlab.figure(bgcolor=(0, 0, 0), size=(800, 450))
show_lidar_with_depth(pc_velo, objects, calib, fig_3d, True, img_width, img_height)
mlab.show()



