# EVA - Assignment 13 - Yolov3 Training


## Problem Statement
1. OpenCV Yolo: [SOURCE](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/)
	1. Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 
	2. Run this image through the code above. 
	3. Upload the link to GitHub implementation of this
	4. Upload the annotated image by YOLO. 
2. Share your NEWLY annotated (same as 12, but annotated using new tool) images with Zoheb by Wednesday at midnight. Take the set back for training on Thursday.
3. Training Custom Dataset on Colab for YoloV3
	1. Refer to this Colab File: [LINK](https://colab.research.google.com/drive/1LbKkQf4hbIuiUHunLlvY-cc0d_sNcAgS)
	2. Refer to this GitHub [Repo](https://github.com/theschoolofai/YoloV3)
	3. Collect a dataset from the last assignment and re-annotate them. Steps are explained in the readme.md file on GitHub.
	4. Once done
		1. [Download](https://www.y2mate.com/en19) a very small (10-30sec) video from youtube which shows your classes
		2. Use [ffmpeg](https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence) to extract frames from the video. 
		3. Upload on your drive (alternatively you could be doing all of this on your drive to save upload time)
		4. Infer on these images using detect.py file. **Modify** detect.py file if your file names do not match the ones mentioned on GitHub. 
			python detect.py --conf-thres 0.3 --output output_folder_name
		6. Use [ffmpeg](https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence)  to convert the files in your output folder to video
		7. Upload the video to YouTube. 
		8. Share the link to your GitHub project with the steps as mentioned above
		9. Share the link to your YouTube video
		10. Share the link of your YouTube video on LinkedIn, Instagram, etc! You have no idea how much you'd love people complimenting you! 
[Bonus: YoloV4 Training on Colab](https://colab.research.google.com/drive/1b08y_nUYv5UtDY211NFfINY7Hy_pgZDt#scrollTo=1YW7jPF1BOAw) 

## OpenCv Yolo

Notebook: https://github.com/vigneshbabupj/EVA5/blob/master/S13/Part%20A/EVA_S13_A_openCv_Yolo_COCO.ipynb

Image
![My_Image](https://github.com/vigneshbabupj/EVA5/blob/master/S13/images/me.jpg)


##  Training Yolov3 on Custom Dataset

Classes:
* hardhat
* mask
* vest
* boot

Notebook: https://github.com/vigneshbabupj/EVA5/blob/master/S13/Part%20B/EVA_S13_B_YoloV3Sample.ipynb

youtube video: https://youtu.be/ZI1nimTUWsE 