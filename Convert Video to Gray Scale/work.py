import shutil
import os 
from matplotlib import pyplot as plt
import time
import cv2

# Function to convert to gray scale 

def convert_to_gray_scale(video_path):
    video = cv2.VideoCapture(video_path)
   


    while True: 
        ret, frame = video.read()
        if ret: 
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('temp',gray)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else : 
            break

    video.release()
  


# Create copies of video files 10,20,30,40,50 and note time taken 
data = {}
for i in range(5):
    os.mkdir(f'{i+1}10th')
    start = time.time()
    for j in range(10*(i+1)):
        shutil.copy(src='temp.mp4',dst=f'./{i+1}10th/temp{j}.mp4')
      
        convert_to_gray_scale(f'./{i+1}10th/temp{j}.mp4')
    end = time.time()
    data [f'{10*(i+1)} Videos'] = end - start


data = {'10 Videos': 15.415261030197144, '20 Videos': 30.092771768569946, '30 Videos': 
50.22762632369995, '40 Videos': 67.00322914123535, '50 Videos': 127.21923565864563}
plt.xlabel('Number of Files')
plt.ylabel('Time taken')
plt.title('Time taken to convert colored videos to gray scale videos')
plt.plot(list(data.keys()),list(data.values()))
plt.show()


