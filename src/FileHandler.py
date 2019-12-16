import random
import csv

def saveScore(name,score):
    with open("scores.csv", "a") as file:
        file.write("{},{}".format(str(name),str(score)))
        file.write("\n")
        file.close()



def readScore():
    with open("scores.csv", "r") as file:
        scoreData = []
        for lines in file:
            try:
                fields = lines.split(",")
                name = fields[0]
                score = int(fields[1])
                scoreData.append((name,score))
            except ValueError:
                score = 0


        file.close()
    return scoreData


def addWord(soal):
    with open("soalhang.txt", "a") as file:
        file.write(soal)
        file.write("\n")
        file.close()

def getWord():
    with open("soalhang.txt","r") as baca:
        listOfSoal = baca.readlines()
        choice = random.choice(listOfSoal)
        baca.close()
    return(choice.rstrip())
