import os
import cv2
path = "C:/Users/nshan/Downloads/Images1"
Images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)
        
print(len(Images))
count = len(Images)
frame = cv2.imread(Images[0])
height,width,layers = frame.shape()
size = (width,height)
print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8,size)
for i in range(0,count-1):
    cv2.imread(i)
    out.write(i)
    print("Done")