import time
import random
import FileHandler
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

w = 0
randList = []
while(w < 5):
    randomWord = FileHandler.getWord()
    randList.append(randomWord)
    time.sleep(1)
    w+=1
print(randList)

