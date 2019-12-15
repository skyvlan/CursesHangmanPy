import random

def saveScore(name,score):
    with open("scores.csv", "a") as file:
        file.write("{},{}".format(str(name),str(score)))
        file.write("\n")
        file.close()



def readScore():
    with open("scores.csv", "r") as file:
        scoreList = file.readlines()
        file.close()
    return scoreList


def addWord(soal):
    with open("soalhang.txt", "a") as file:
        file.write(soal)
        file.close()

def getWord():
    with open("soalhang.txt","r") as baca:
        listOfSoal = baca.readlines()
        choice = random.choice(listOfSoal)
        baca.close()
    return(choice.rstrip())
