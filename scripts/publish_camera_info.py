#!/usr/bin/env python

import rospy
import rospkg
import yaml
from sensor_msgs.msg import CameraInfo

if __name__ == '__main__':
    try:
        rospy.init_node('camera_info_publisher', anonymous=True)
        pub = rospy.Publisher('camera/camera_info', CameraInfo, queue_size=1)
        rate = rospy.Rate(10)
        rospack = rospkg.RosPack()

        camera_params_file = rospack.get_path('stag_ros') + "/param/camera_params.yaml"

        # Load data from file
        with open(camera_params_file, "r") as file_handle:
            calib_data = yaml.load(file_handle)
        # Parse
        camera_info_msg = CameraInfo()
        camera_info_msg.width = calib_data["image_width"]
        camera_info_msg.height = calib_data["image_height"]
        camera_info_msg.K = calib_data["camera_matrix"]["data"]
        camera_info_msg.D = calib_data["distortion_coefficients"]["data"]
        camera_info_msg.R = calib_data["rectification_matrix"]["data"]
        camera_info_msg.P = calib_data["projection_matrix"]["data"]
        camera_info_msg.distortion_model = calib_data["distortion_model"]

        while not rospy.is_shutdown():
            pub.publish(camera_info_msg)
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
