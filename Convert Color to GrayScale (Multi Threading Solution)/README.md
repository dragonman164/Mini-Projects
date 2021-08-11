# Multithreading Solution to convert colored images to gray scale and analysis

This project converts colored images to gray scale images and notes the time taken for the same.



## Install dependencies using pip
```
pip install matplotlib
pip install python-opencv
```


## Results
The results were taken for 500 files

| Number of Threads | Time Taken | 
| ------------- | --------- |
| 5  | 3.7109994888305664 s  | 
| 10  | 2.9890599250793457 s |   
| 15  | 2.7537753582000732 s   |  
| 20  | 2.7324788570404053 s   |
| 25  | 2.789254665374756 s   |


<br>

## Graphical  Representation for number of files vs time taken 
<br>

 <img width="1604" src="./Figure_1.png"> 

<br>
Conclusion : The time taken for converting files to gray scale first increases , then decreases by increasing threads. This is because at the beginning, parellism is achieved but later, the context switches time increasing due to frequent switching and time increases.
<br>

## Command Line Solution
To use the command line solution 
```
python <script>.py inputdir outputdir no_of_threads
```
