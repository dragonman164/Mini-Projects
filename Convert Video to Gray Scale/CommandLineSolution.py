import os
import sys
import time
import shutil
import cv2
start_time = time.time()

time_var=0
arguments = sys.argv
if len(arguments) != 3:
    print("To Execute the script use the following syntax: ")
    print("python <nameoffile>.py in_directory out_directory")
else :

    in_directory = arguments[1]
    out_directory=arguments[2]
    
    videos=os.listdir(in_directory)
    
    os.mkdir(out_directory)
    x=len(os.listdir(in_directory))
    counter=0
    

    for video in videos:

        

        cap = cv2.VideoCapture(f'{in_directory}/{video}')
        
        
        

        # li = os.listdir(
        #     '/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Mini_Proj_5-Convert multiple videos to grayscale/video_dir')
        # print(li)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

        
        out = cv2.VideoWriter(out_directory+'/'+'output' + str(counter) + '.mp4', fourcc, 20.0, (640, 480))
        
        counter+=1

        while (cap.isOpened()):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            #dstPath=join(out_directory,out)
            out.write(frame)
            
            #cv2.imwrite(dstPath,gray)
            #cv2.imwrite(f'{out_directory}/{video}',gray)
            cv2.imshow('frame', gray)
            
            

            

            time_var=time.time()-start_time
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break



cap.release()
out.release()
cv2.destroyAllWindows()
