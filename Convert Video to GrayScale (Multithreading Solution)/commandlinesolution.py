import sys 
import threading
from queue import Queue
import threading
import os
import time
import cv2



def task(video_path,inp):
    video = cv2.VideoCapture(f'./{inp}/{video_path}')
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

# Function to send task to threads
def do_stuff(q,inp):
    while not q.empty():
        value = q.get()
        task(value,inp)
        q.task_done()


arguments = sys.argv
if len(arguments) != 3 : 
    print("""Format : 
    py <script.name>.py inputfile  no_of_threads
    """)
else:
    inputDir = arguments[1]
    threads = int(arguments[2])

# Loop For Number of Threads
t = threads
jobs = Queue()
for elem in os.listdir(inputDir):
    jobs.put(elem)
start = time.time()
for i in range(t):
    worker = threading.Thread(target=do_stuff, args=(jobs,inputDir))
    worker.start()

jobs.join()
end = time.time()
print("Time Taken", end - start)
print("Finished.....")

