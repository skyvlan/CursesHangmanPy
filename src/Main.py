import curses
import os
import time
import GameEngine
import GameHandler
import FileHandler

renderer = GameEngine.RenderInitializer()

def MainMenu():
    TitleString = "Hangman V0.0.1a"
    MenuString1 = "1. Play Game"
    MenuString2 = "2. Add Words"
    MenuString3 = "3. Exit Game"
    mainMenuborder = GameEngine.RenderObject()
    mainMenuObj = GameEngine.RenderObject()
    menuInput = GameEngine.InputHandler()
    while(True):
        mainMenuborder.drawBorderWr()
        mainMenuObj.drawObjectWr((renderer.xBorder // 2) - len(TitleString), (renderer.yBorder//2) - 5, TitleString)
        mainMenuObj.drawObjectWr((renderer.xBorder // 2) - len(MenuString1), (renderer.yBorder // 2) - 3,  MenuString1)
        mainMenuObj.drawObjectWr((renderer.xBorder // 2) - len(MenuString2) , (renderer.yBorder // 2) - 2 , MenuString2)
        mainMenuObj.drawObjectWr((renderer.xBorder // 2) - len(MenuString3), (renderer.yBorder // 2) - 1, MenuString3)
        renderer.refresh()
        if(chr(menuInput.getInput()) == "1"):
            break
        else:
            exit()


def Game():
    Hangman = GameEngine.RenderObject()
    Answer = GameEngine.RenderObject()
    border = GameEngine.RenderObject()
    input = GameEngine.InputHandler()
    health = GameEngine.RenderObject()
    debugObj = GameEngine.RenderObject()
    hangmanState = GameEngine.RenderObject()
    GameObject = GameHandler.Game()
    GameObject.setCurrentWord("radya")
    correctAns = 0
    UnansweredWord = GameObject.unanswered
    while(GameObject.checkifAnswerCorrect() == False):
        border.drawBorderWr()
        UnansweredStr = " ".join(UnansweredWord)
        Hangman.drawObjectWr((renderer.xBorder//2) - 20, (renderer.yBorder//2) - 5, GameObject.hangman[GameObject.hangmanState])
        health.drawObjectWr(2,2, str(GameObject.health))
        hangmanState.drawObjectWr(2,3, str(GameObject.hangmanState))
        Answer.drawObjectWr((renderer.xBorder // 2), (renderer.yBorder // 2) - 5, UnansweredStr.upper())
        renderer.refresh()
        ans = chr(input.getInput())
        try:
            #index = GameObject.wordList.index(ans)
            index = [i for i, x in enumerate(GameObject.wordList) if x == ans]
            for j in index:
                UnansweredWord[j] = ans
            debugObj.drawObjectWr(2, 5, str(UnansweredWord))
            renderer.refresh()
        except ValueError:
            GameObject.damagePlayer()
        renderer.updateFrame()
Game()
# testlist = ['r', 'a', 'd','y','a']
# EmptyList = ["_","_","_","_","_"]
# index = [i for i, x in enumerate(testlist) if x == 'a']
# for j in index:
#     EmptyList[j] = 'a'
# print(EmptyList)