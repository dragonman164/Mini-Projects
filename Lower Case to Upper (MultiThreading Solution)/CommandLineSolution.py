import sys 
import threading
from queue import Queue
import threading
import shutil
import os
import time



def task(filename,inp,out):
    inputFile = open(f"./{inp}/{filename}", "r")
    content = inputFile.read()
    outputFile = open(f"./{out}/{filename}", "w")
    outputFile.write(content.upper())  


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
os.mkdir(outpurDir)
for elem in os.listdir(inputDir):
    jobs.put(elem)
start = time.time()
for i in range(t):
    worker = threading.Thread(target=do_stuff, args=(jobs,inputDir,outpurDir))
    worker.start()

jobs.join()
end = time.time()
print("Time Taken", end - start)
print("Finished.....")

