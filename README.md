# Hot Topics in Computer Vision (Project B)
### "Autonomous Driving: Tell me what you are able to see!"

In this student project, an autonomous driving challenge – the parking pilot – will be analyzed in detail. Therefore, different sub-functions for parking lot recognition and status assessment (free, occupied) should be implemented. Data from different sensors shall be used to identify and extract features. With the help of data fusion, a provided map shall be verified and updated with free parking spaces.

The main challenge of the project is to deal with the characteristics of different sensors. What is each sensor able to “see”? What are the strengths and weaknesses of the sensors?

### Participants list
**Camera group**  
[Lei Kang](https://github.com/kangleigithub)  
[Jiaqiao Peng](https://github.com/PengJiaqiao)  
[Furkan Kilicaslan](https://github.com/Klcsln)  
[Rudhishna Narayanan Nair](https://github.com/rudhi31)  
[Daniel Sharkov](https://github.com/dsharkovv)  

### YOLOv3 (You only look once)
YOLO is a state-of-the-art, real-time object detection system. This model has several advantages over classifier-based systems. It looks at the whole image at test time so its predictions are informed by global context in the image. It also makes predictions with a single network evaluation unlike systems like R-CNN which require thousands for a single image. This makes it extremely fast, more than 1000x faster than R-CNN and 100x faster than Fast R-CNN. YOLOv3 is the latest variant of this popular object detection algorithm.

**(Attention, this is OBJECT - DETECTION. I said it clearly and wrote this as the name of cpp file. I don't know why my teammate thought it was segmentation and I also wandered who proposed using segmentation. It was totally useless and wasted a lot of time because we don't need such pixel-level detection. Whatever, let this course go.)**

Starting with OpenCV 3.4.2, we can easily use `opencv_dnn` module to load YOLOv3 pre-trained models in our own cpp application. The model was trained on COCO dataset by [Darknet: an open source neural network framework written in C and CUDA](https://pjreddie.com/darknet/). Download [weights file](https://drive.google.com/open?id=1lAivsJldk6Gve_SwNVAj_efgHm-dNgbS) and put it as well as other configuration files `yolov3.cfg`, `coco.names` into the path shown in `/Camera_Project/new_station/src/object_detection_yolo.cpp`.

You can simply use `./YOLOv3/object_detection_yolo.out --video=PMD_Example_left.avi` for inference under linux environment. The output will be like as follows. The average FPS is around 4.3, with my i7-6700HQ CPU only.

<img src="https://user-images.githubusercontent.com/26578566/54872520-66329d80-4dc5-11e9-9d56-b7e811d50bc6.png" width="1920">  

### TODO
The conversion of the coordinates is still not completed. And may be never completed. **Because this team is like a shit and only two of us were working on it. One man quited. One man left Berlin and said he can't use computer. One man set up the environment this week (March 23). What can I do?**

**Finally I understood. Teamwork is like a prisoner's dilemma.**

### Reference

	@article{YOLOv3,  
	  title={YOLOv3: An Incremental Improvement},  
	  author={J Redmon, A Farhadi },
	  year={2018}
