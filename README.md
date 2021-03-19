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
<node pkg="image_transport" type="republish" name="republish" args="compressed in:=/raspicam_node/image raw out:=/raspicam_node/image"/>
