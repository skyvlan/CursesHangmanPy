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
        logoDrawer.drawObject(renderer.xBorder//2-len("H A N G M A N")//2, renderer.yBorder//2-4, "H A N G M A N", GameEngine.WR)
        key = input.getInput()
        if key == curses.KEY_UP and row > 0:
            row -= 1
        elif key == curses.KEY_DOWN and row < len(menuSelection)-1:
            row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:

            break
        printMenu(row)

    return row





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
    while(GameObject.health > 0):
        currentWord = FileHandler.getWord()
        GameObject.setCurrentWord(currentWord)
        UnansweredWord = GameObject.unanswered
        while(GameObject.checkifAnswerCorrect() == False):
            border.drawBorder(GameEngine.WR)
            HighscoreStr = "SCORE : " + str(GameObject.score)
            UnansweredStr = " ".join(UnansweredWord)
            hangmanArt = GameObject.hangman[GameObject.hangmanState].splitlines()
            for yPos, lines in enumerate(hangmanArt):
                Hangman.drawObject(15, (renderer.yBorder//2) - 4 + yPos, lines, GameEngine.WR)
            hangmanBox.drawRect(28, (renderer.yBorder//2)-4 , 12, 10)
            score.drawObject(renderer.xBorder//2 - len(HighscoreStr)//2, 1, HighscoreStr, GameEngine.WR)
            health.drawObject(2,2, str(GameObject.health), GameEngine.WR)
            hangmanState.drawObject(2,3, str(GameObject.hangmanState), GameEngine.WR)
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
            debugObj.drawObject(2, 5, str(UnansweredWord), GameEngine.WR)
            renderer.refresh()
            renderer.updateFrame()
            if(GameObject.health < 0):
                time.sleep(5)
                return GameObject.score
                break
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

    border.drawBorder()
    LeaderboardTitle.enableColor(GameEngine.PAIR_HIGHLIGHT)
    LeaderboardTitle.drawObject(renderer.xBorder // 2 - len("LEADERBOARD")//2, renderer.yBorder // 2 - 13, "LEADERBOARD")
    renderer.refresh()
    time.sleep(10)

select = MainMenu()
if select == 0:
    score = Game()
    GameOver(score)

elif select == 1:
    exit()
elif select == 2:
    Leaderboard()
elif select == 3:
    exit()

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

