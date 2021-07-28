import string
import shutil
import os
import time
from matplotlib import pyplot as plt


# Step 1 : Generate a 10 MB Text File 

f = open("temp.txt",'w')

alphabets = string.ascii_letters

for i in range(200000):
    f.writelines(alphabets + '\n')

# Step 2 : Create 1K,2K,3K,4K,5K Copies of each text file
for i in range(5):
    os.mkdir(f'{i+1}Kfiles')
    for j in range((i+1)*100):
        shutil.copyfile(src='temp.txt',dst=f'D:\\Projects\\TextFileProject\\{i+1}KFiles\\copy{j+1}.txt')


# Step 3 : Convert Given Files to Upper Case and Note Time Taken
data = {}

for i in range(5):
    files = os.listdir(f'{i+1}Kfiles')
    start = time.time()
    for file in files:
        inputFile = open(f"{i+1}Kfiles/{file}", "r")
        content = inputFile.read()
        with open(f"{i+1}Kfiles/{file}", "w") as outputFile:
                outputFile.write(content.upper())  
    end = time.time()
    data[i+1] = end - start
    print(f"Time Taken to Convert to Upper Case {i+1}K Files", end - start)

# Step 4 : Plot the required Data
print(data)

plt.plot(list(data.keys()),list(data.values()))
plt.xlabel("K Files")
plt.ylabel("Time taken to convert to upper case")
plt.title("Files vs Time")
plt.show()