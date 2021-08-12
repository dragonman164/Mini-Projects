import sys 
import threading
from queue import Queue
import threading
import os
import time
import cv2



def task(filename,inp,out):
    check = cv2.imread(f'./{inp}/{filename}')
    gray = cv2.cvtColor(check,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'./{out}/{filename}',gray)


# Function to send task to threads
def do_stuff(q,inp,out):
    while not q.empty():
        value = q.get()
        task(value,inp,out)
        q.task_done()


arguments = sys.argv
if len(arguments) != 4 : 
    print("""Format : 
    py <script.name>.py inputdir outputdir no_of_threads
    """)
else:
    inputDir = arguments[1]
    outpurDir = arguments[2]
    threads = int(arguments[3])

# Loop For Number of Threads
t = threads
jobs = Queue()
os.mkdir('output')
for elem in os.listdir('input'):
    jobs.put(elem)
start = time.time()
for i in range(t):
    worker = threading.Thread(target=do_stuff, args=(jobs,inputDir,outpurDir))
    worker.start()

jobs.join()
end = time.time()
print("Time Taken", end - start)
print("Finished.....")

