import shutil
import os
import time
from matplotlib import pyplot as plt
from queue import Queue
import threading
import cv2


# Function to Convert the Image to Gray Scale
def task(filename):
    start = time.time()
    check = cv2.imread(f'./input/{filename}')
    gray = cv2.cvtColor(check,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'./output/{filename}',gray)


   
# Function to send task to threads
def do_stuff(q):
    while not q.empty():
        value = q.get()
        task(value)
        q.task_done()

# Step 1 : Generate 500 Images 
os.mkdir('input')
for j in range(500):
    shutil.copy("./check.jpg",dst=f"./input/copy{j}.jpg")




# Step 3 : Convert Images to Gray Scale and note the time taken
data = {}

for t in [j*5 for j in range(1,6)]:
    jobs = Queue()
    os.mkdir('output')
    for elem in os.listdir('input'):
        jobs.put(elem)
    start = time.time()
    for i in range(t):
        worker = threading.Thread(target=do_stuff, args=(jobs,))
        worker.start()
    
    jobs.join()
    end = time.time()
    print(t, end - start)
    data[t] = end - start
    shutil.rmtree('output')


# Step 4 : Plot the required Data
print(data)

plt.plot(list(data.keys()),list(data.values()))
plt.xlabel("Number of threads")
plt.ylabel("Time Taken")
plt.title("Time taken to convert 100 Images from color to gray Scale")
plt.show()