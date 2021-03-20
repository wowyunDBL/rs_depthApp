## 0319
1. connected in USB 2.1
```
[ INFO] [1616143122.262192915]: Device with physical ID 1-2.1-23 was found.
[ INFO] [1616143122.262256711]: Device with name Intel RealSense D435 was found.
[ INFO] [1616143122.264078117]: Device with port number 1-2.1 was found.
[ INFO] [1616143122.264216074]: Device USB type: 2.1
[ WARN] [1616143122.264292838]: Device 832412070163 is connected using a 2.1 port. Reduced performance is expected.
[ INFO] [1616143122.264484801]: Resetting device...
```

2. file log:
```
├── camera-realsense2_camera-2-stdout.log  \\process died log  
├── known_hosts \\remove this when cannot ssh, directly detele  
├── lab-0319-short.bag  
├── lab-3.bag  
├── lab-.bag  
├── round1.bag \\go straight  
├── round2.bag \\turn 90 degree  
├── round3.bag \\turn 2 90 degree  
└── round4.bag \\with video   
 
```

3. compressed depth rosmsg cannot directly use image_transport of raw:
```
[ WARN] [1616234838.896853954]: OGRE EXCEPTION(2:InvalidParametersException): Stream size does not match calculated image size in Image::loadRawData at /build/ogre-1.9-mqY1wq/ogre-1.9-1.9.0+dfsg1/OgreMain/src/OgreImage.cpp (line 283)
[ERROR] [1616234838.896968606]: Error loading image: OGRE EXCEPTION(2:InvalidParametersException): Stream size does not match calculated image size in Image::loadRawData at /build/ogre-1.9-mqY1wq/ogre-1.9-1.9.0+dfsg1/OgreMain/src/OgreImage.cpp (line 283)
```

