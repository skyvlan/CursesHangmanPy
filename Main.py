import curses
import os
import time
import GameEngine
import GameHandler
import FileHandler


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
            dbgText.drawObject(2, y+1, "Row:{} X:{} Y:{}".format(row, x, y))
            selection.enableColor(GameEngine.PAIR_HIGHLIGHT, GameEngine.WR)
            selection.drawObject(x,y, row,GameEngine.WR)
            selection.disableColor(GameEngine.PAIR_HIGHLIGHT, GameEngine.WR)
        else:
            dbgText.drawObject(2, y + 1, "Row:{} X:{} Y:{}".format(row, x, y))
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
    while(GameObject.health != 0):
        GameObject.setCurrentWord("Test")
        UnansweredWord = GameObject.unanswered
        while(GameObject.checkifAnswerCorrect() == False):
            border.drawBorder(GameEngine.WR)
            UnansweredStr = " ".join(UnansweredWord)
            Hangman.drawObject((renderer.xBorder//2) - 20, (renderer.yBorder//2) - 5, GameObject.hangman[GameObject.hangmanState], GameEngine.WR)
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
            debugObj.drawObject(2, 5, str(UnansweredWord), GameEngine.WR)
            renderer.refresh()
            renderer.updateFrame()


def GameOver():
    renderer.erase()
    border = GameEngine.RenderObject()
    GameOver = GameEngine.RenderObject()
    border.drawBorder()
    GameOver.drawObject((renderer.xBorder//2) - len("Game Over!"), renderer.yBorder//2, "Game Over!")
    time.sleep(10)
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
    Game()
    Leaderboard()

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

