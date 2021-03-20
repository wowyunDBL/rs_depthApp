# rs_depthApp
## 0314  
git add <file>  
git commit -m ""  
git push -u  
git remote -v //check remote  
git remote add origin https://github.com/wowyunDBL/rs_depthApp.git

rosrun rviz rviz -d `rospack find depth_app`/rs.rviz  
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud align_depth:=true  
rosrun rqt_reconfigure rqt_reconfigure

rosbag record /camera/color/image_raw /camera/depth/image_rect_raw /camera/depth/color/points /camera/aligned_depth_to_color/image_raw /tf_static /tf  

rosrun depthApp_node test_cbImg.py True  

## save compressed  
```
<node pkg="image_transport" type="republish" name="republish" args="compressed in:=/camera/color/image_raw/compressed raw out:=/camera/color/image_raw/image"/>
# check package
anny@anny-hehe:~$ roscd compressed_
compressed_depth_image_transport/
compressed_image_transport/
\#such as package ros-kinetic-compressed-image-transport

```

## 0319 
```
ping 192.168.0.1xx
ssh ursrobot@192.168.0.1xx

roslaunch realsense2_camera rs_camera.launch

rosbag record /camera/color/image_raw/compressed /camera/depth/image_rect_raw/compressed /camera/depth/color/points /camera/aligned_depth_to_color/image_raw/compressed /tf_static /tf /imu/data /husky_velocity_controller/odom /navsat/fix
```







