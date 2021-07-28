import os 
import time
import sys

arguments = sys.argv
if len(arguments) != 3:
    print("To Execute the script use the following syntax: ")
    print("py <nameoffile>.py indir outdir")
else :

    in_directory = arguments[1]
    out_directory = arguments[2]

    os.mkdir(out_directory)
    files = os.listdir(in_directory)
    start = time.time()
    for file in files:
        inputFile = open(f"{in_directory}/{file}","r")
        content = inputFile.read()
        outFile = open(f"{out_directory}/{file}","w")
        outFile.write(content.upper())

    end = time.time()
    print(f"Time Taken to Convert to Upper Case", end - start)