import string
import shutil
import os
import time
from matplotlib import pyplot as plt
from queue import Queue
import threading

# Function to Convert the File to Upper Case
def task(filename):
    inputFile = open(f"./input/{filename}", "r")
    content = inputFile.read()
    outputFile = open(f"./output/{filename}", "w")
    outputFile.write(content.upper())  

   
# Function to send task to threads
def do_stuff(q):
    while not q.empty():
        value = q.get()
        task(value)
        q.task_done()

# Step 1 : Generate a 10 MB Text File 

f = open("temp.txt",'w')

alphabets = string.ascii_letters

for i in range(200000):
    f.writelines(alphabets + '\n')

# Step 2 : Create 50 Files
os.mkdir(f'input')
for j in range(100):
    shutil.copyfile(src='temp.txt',dst=f'./input/temp{j}.txt')


# Step 3 : Convert Given Files to Upper Case and Note Time Taken
data = {}

for t in [j*5 for j in range(1,5)]:
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
plt.title("Time taken to convert to 500 files to Upper Case")
plt.show()