import random
def addsoal(x):
    with open("soalhang.txt","r") as soal:
        f = soal.read()
        soal.close()
    with open("soalhang.txt","w") as soal:
        soal.write(f)
        soal.write(x)
        soal.write("\n")
        soal.close()
    with open("soalhang.txt","r") as soal:
        f = soal.read()
        soal.close()
    return(f)

def splitletter(word):
    tmp=[]
    for i in word:
        try:
            ind = tmp.index(i)
        except:
            tmp.append(i)
    return tmp

def getWord():
    with open("soalhang.txt","r") as baca:
        listOfSoal = baca.readlines()
        choice = random.choice(listOfSoal)
        return(choice.rstrip())