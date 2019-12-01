import curses
import os
import time
import GameEngine
import GameHandler

renderer = GameEngine.RenderInitializer()
Hangman = GameEngine.RenderObject()
Answer = GameEngine.RenderObject()
border = GameEngine.RenderObject()
input = GameEngine.InputHandler()
health = GameEngine.RenderObject()
hangmanState = GameEngine.RenderObject()
GameObject = GameHandler.Game()
GameObject.setCurrentWord("Test")
correctAns = 0
UnansweredWord = GameObject.unanswered
while(correctAns != GameObject.WordLength):
    border.drawBorderWr()
    UnansweredStr = " ".join(UnansweredWord)
    Hangman.drawObjectWr((renderer.xBorder//2) - 20, (renderer.yBorder//2) - 5, GameObject.hangman[GameObject.hangmanState])
    health.drawObjectWr(2,2, str(GameObject.health))
    hangmanState.drawObjectWr(2,3, str(GameObject.hangmanState))
    Answer.drawObjectWr((renderer.xBorder // 2), (renderer.yBorder // 2) - 5, UnansweredStr)
    renderer.refresh()
    ans = chr(input.getInput())
    try:
        index = GameObject.wordList.index(ans)
        UnansweredWord[index] = ans
    except ValueError:
        GameObject.damagePlayer()
    renderer.updateFrame()







