import time
import random
def dev(a,b):
    try:
     print("Hasil" , a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
def recursiveFactorial(no):
    if no == 1:
        return 1
    else:
        print(no)
        return no * recursiveFactorial(no-1)

def selectionsort(aList):
    for i in range(len(aList)-1,0,-1):
        posisiMax = 0
        for j in range(1, i+1):
            if aList[j]>aList[posisiMax]:
                posisiMax = j
        temp = aList[i]
        aList[i]=aList[posisiMax]
        aList[posisiMax]=temp



a = [32,55,225,67,32,12,4,97]
res = [random.randrange(1, 1024, 1) for i in range(2048)]
startTime = time.time()
selectionsort(res)
endTime = time.time()
execTime = int((endTime - startTime) * 1000)
print(execTime)
print(res)
