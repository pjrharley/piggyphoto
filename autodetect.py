from __future__ import print_function
import piggyphoto as pp

print("libgphoto2 version:")
print(pp.library_version())

print("detected cameras:")
cameras = pp.CameraList(autodetect=True)
print(cameras)
