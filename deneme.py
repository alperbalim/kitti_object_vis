from xvfbwrapper import Xvfb
from mayavi import mlab
import numpy as np
import time



# Create some data
x, y, z = np.mgrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)

# Create a 3D visualization using Mayavi's mlab
mlab.figure(bgcolor=(1, 1, 1))
mlab.contour3d(s, contours=8, transparent=True, colormap='viridis')

# Show the Mayavi GUI window
mlab.show()
time.sleep(25)
# Stop the virtual display
vdisplay.stop()
