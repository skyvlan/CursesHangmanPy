import curses
import os
import time
import GameEngine
import GameHandler
import FileHandler
import random
import string

renderer = GameEngine.RenderInitializer()
menuSelection = ["Play Game", "Add Word", "Leaderboard", "Exit"]
cheat = True
title = """
 _   _   ___   _   _ _____ ___  ___  ___   _   _ 
| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
| | | || | | || |\  | |_\ \| |  | || | | || |\  |
\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
""".splitlines()
def printMenu(selected_row):
    renderer.erase()
    dbgText = GameEngine.RenderObject()
    selection = GameEngine.RenderObject()
    for i, row in enumerate(menuSelection):
        x = renderer.xBorder//2 - len(row)//2
        y = (renderer.yBorder//2 - len(menuSelection)//2 + i) + 3
        if i == selected_row:
            #dbgText.drawObject(2, y+1, "Row:{} X:{} Y:{}".format(row, x, y))
            selection.enableColor(GameEngine.PAIR_HIGHLIGHT, GameEngine.WR)
            selection.drawObject(x,y, row,GameEngine.WR)
            selection.disableColor(GameEngine.PAIR_HIGHLIGHT, GameEngine.WR)
        else:
           # dbgText.drawObject(2, y + 1, "Row:{} X:{} Y:{}".format(row, x, y))
            selection.drawObject(x, y, row, GameEngine.WR)

    renderer.refresh()

def MainMenu():
    renderer.erase()
    row = 0
    selectedRow = 0
    printMenu(row)
    input = GameEngine.InputHandler()
    dbgText = GameEngine.RenderObject()
    logoDrawer = GameEngine.RenderObject()
    border = GameEngine.RenderObject()
    box = GameEngine.RenderObject()
    border.drawBorder()
    while(True):
        box.drawRect(54, 15, 12, 5, GameEngine.WR)
        border.drawBorder(GameEngine.WR)
        for yPos, lines in enumerate(title):
            logoDrawer.drawObject((renderer.xBorder//2) - 25, 5+yPos, lines, GameEngine.WR)
        key = input.getInput()
        if key == curses.KEY_UP and row > 0:
            row -= 1
        elif key == curses.KEY_DOWN and row < len(menuSelection)-1:
            row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:

            break
        printMenu(row)

    return row


def addSoal():
    curses.endwin()
    print("Welcome to Add Word Console.")
    print("Available Commands:  console_help, console_exit, console_cls")
    print("type your word to be added to the game! The character limit is 16 Characters")
    print("type console.help to display this message again")
    while(True):
        command = input(">").lower()
        if command ==  "console_help":
            print("Available Commands:  console_help, console_exit, console_cls")
            print("type your word to be added to the game!")
            print("type console.help to display this message again")
        elif command == "console_exit":
            main()
        elif command == "console_cls":
            os.system("cls")
        elif command == "console_guagoblok":
            cheat = True
        else:
            try:
                if len(command) > 16:
                    print("Character limit is 16 Characters!")
                elif not command.isalpha() and not command == "" and not command.isspace():
                    print("You cannot input numbers and/or symbols!")
                elif command.isspace() or command == "":
                    continue
                else:
                    FileHandler.addWord(command)
                    print("Word", command, "added Succesfully!")
            except IOError:
                print("Error in Writing File. (Unable to open file) Exception: IOError")



def Game():
    renderer.erase()
    Hangman = GameEngine.RenderObject()
    Answer = GameEngine.RenderObject()
    border = GameEngine.RenderObject()
    input = GameEngine.InputHandler()
    health = GameEngine.RenderObject()
    debugObj = GameEngine.RenderObject()
    hangmanState = GameEngine.RenderObject()
    GameObject = GameHandler.Game()
    score = GameEngine.RenderObject()
    hangmanBox = GameEngine.RenderObject()
    lose = False
    while(lose == False):
        currentWord = FileHandler.getWord()
        GameObject.setCurrentWord(currentWord)
        UnansweredWord = GameObject.unanswered
        spaceIndex = [i for i, x in enumerate(GameObject.wordList) if x == " "]
        for l in spaceIndex:
            UnansweredWord[l] = " "

        while(GameObject.checkifAnswerCorrect() == False):
            border.drawBorder(GameEngine.WR)
            if cheat == True:
                cheatStr = "word: {}"
                score.drawObject(1, 1, cheatStr.format(GameObject.word), GameEngine.WR)
            HighscoreStr = "SCORE : " + str(GameObject.score)
            UnansweredStr = " ".join(UnansweredWord)
            hangmanArt = GameObject.hangman[GameObject.hangmanState].splitlines()
            for yPos, lines in enumerate(hangmanArt):
                Hangman.drawObject(15, (renderer.yBorder//2) - 4 + yPos, lines, GameEngine.WR)
            hangmanBox.drawRect(28, (renderer.yBorder//2)-4 , 12, 10)
            score.drawObject(renderer.xBorder//2 - len(HighscoreStr)//2, 1, HighscoreStr, GameEngine.WR)
            #health.drawObject(2,2, str(GameObject.health), GameEngine.WR)
            #hangmanState.drawObject(2,3, str(GameObject.hangmanState), GameEngine.WR) #DEBUG
            Answer.drawObject((renderer.xBorder // 2), (renderer.yBorder // 2) - 5, UnansweredStr.upper(), GameEngine.WR)
            renderer.refresh()
            ans = chr(input.getInput())
            #index = GameObject.wordList.index(ans)
            index = [i for i, x in enumerate(GameObject.wordList) if x == ans]
            if index == []:
                GameObject.damagePlayer()
            for j in index:
                UnansweredWord[j] = ans
                GameObject.score += len(ans) * 10
            #debugObj.drawObject(2, 5, str(UnansweredWord), GameEngine.WR)
            renderer.refresh()
            renderer.updateFrame()
            if (GameObject.health == 0):
                border.drawBorder(GameEngine.WR)
                HighscoreStr = "SCORE : " + str(GameObject.score)
                UnansweredStr = " ".join(GameObject.word)
                hangmanArt = GameObject.hangman[GameObject.hangmanState].splitlines()
                for yPos, lines in enumerate(hangmanArt):
                    Hangman.drawObject(15, (renderer.yBorder // 2) - 4 + yPos, lines, GameEngine.WR)
                hangmanBox.drawRect(28, (renderer.yBorder // 2) - 4, 12, 10)
                score.drawObject(renderer.xBorder // 2 - len(HighscoreStr) // 2, 1, HighscoreStr, GameEngine.WR)
                Answer.drawObject((renderer.xBorder // 2), (renderer.yBorder // 2) - 5, UnansweredStr.upper(),
                                  GameEngine.WR)
                renderer.refresh()
                renderer.updateFrame()
                time.sleep(5)
                return GameObject.score


        GameObject.score += 100





def GameOver(score):
    renderer.erase()
    border = GameEngine.RenderObject()
    GameOver = GameEngine.RenderObject()
    yourName = GameEngine.InputHandler()
    border.drawBorder()
    scoreStr = "SCORE : {}".format(score)
    GameOver.drawObject((renderer.xBorder//2) - len("Game Over!")//2, renderer.yBorder//2, "Game Over!")
    GameOver.drawObject((renderer.xBorder // 2) - len(scoreStr) // 2, (renderer.yBorder // 2)+1, scoreStr)
    GameOver.drawObject((renderer.xBorder // 2) - len("Your Name:") // 2, (renderer.yBorder // 2) + 2, "Your Name: ")
    curses.echo()
    curses.curs_set(1)
    name = yourName.getStringInput(((renderer.xBorder // 2) + len("Your Name:")//2) + 1 ,  (renderer.yBorder // 2) + 2)
    curses.curs_set(0)
    curses.noecho()

    FileHandler.saveScore(name.decode("utf-8"), score)
    time.sleep(5)
    Leaderboard()

def Leaderboard():
    renderer.erase()
    border = GameEngine.RenderObject()
    LeaderboardTitle = GameEngine.RenderObject()
    rectangle = GameEngine.RenderObject()
    LeaderboardObj = GameEngine.RenderObject()
    border.drawBorder()
    LeaderboardTitle.enableColor(GameEngine.PAIR_HIGHLIGHT)
    LeaderboardTitle.drawObject(renderer.xBorder // 2 - len("LEADERBOARD")//2, renderer.yBorder // 2 - 13, "LEADERBOARD")
    LeaderboardTitle.disableColor(GameEngine.PAIR_HIGHLIGHT)
    rectangle.drawRect((renderer.xBorder//2) - len("LEADERBOARD") - 10, (renderer.yBorder//2) - 10,40,20)
    scores = FileHandler.readScore()
    scores.sort(key= lambda x: x[1], reverse=True)
    for num, line in enumerate(scores):
        leaderboardLine = "{}. {} ........ SCORE: {}"
        LeaderboardObj.drawObject((renderer.xBorder//2) - len("LEADERBOARD") - 9, (renderer.yBorder//2) - 9 + 2*num, leaderboardLine.format(num+1,line[0].upper(),line[1]))
        if num > 8:
            break
    renderer.refresh()
    time.sleep(10)
    main()

def main():
    select = MainMenu()
    if select == 0:
        score = Game()
        GameOver(score)

    elif select == 1:
        cheat = addSoal()
    elif select == 2:
        Leaderboard()
    elif select == 3:
        exit()

main()
# gameVar = Game()
# while(gameVar == True):
#      Game(Word)
# else:

# testlist = ['r', 'a', 'd','y','a']
# EmptyList = ["_","_","_","_","_"]
# index = [i for i, x in enumerate(testlist) if x == 'a']
# for j in index:
#     EmptyList[j] = 'a'
# print(EmptyList)

