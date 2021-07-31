import sys 
import cv2
import os

arguments = sys.argv
if len(arguments) != 3:
    print("""Enough Arguments not provided
    Format py script <inputdir> <outputdir>
    """)
else:
    inputdir = arguments[1]
    outputdir = arguments[2]
   

    images = os.listdir(inputdir)
    os.mkdir(outputdir)
    for image in images:
        check = cv2.imread(f'./{inputdir}/{image}')
        gray = cv2.cvtColor(check,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'./{outputdir}/{image}',gray)
    print("Job Done !!!!!")

       
     
