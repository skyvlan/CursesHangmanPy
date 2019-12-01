import curses
import os
import GameHandler
import time

class RenderInitializer:

    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(1)
        self.gamespeed = 15 #default Framerate
        self.yBorder, self.xBorder = self.screen.getmaxyx()

    def erase(self):
        time.sleep(1 / self.gamespeed)
        self.screen.erase()
    def refresh(self):
        time.sleep(1/self.gamespeed)
        self.screen.refresh()
    def updateFrame(self):
        time.sleep(1 / self.gamespeed)
        self.screen.refresh()
        self.screen.erase()
    def EndWindow(self):
        curses.endwin()

class RenderObject(RenderInitializer):

    def drawBorder(self):
        self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
        time.sleep(1 / self.gamespeed)
        self.screen.refresh()
    def drawBorderWr(self):
        self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
    def drawObject(self, Xpos, Ypos, Text):
        self.screen.addstr(Ypos, Xpos, Text)
        time.sleep(1 / self.gamespeed)
        self.screen.refresh()
    def drawObjectWr(self, Xpos, Ypos, Text):
        self.screen.addstr(Ypos, Xpos, Text)




class InputHandler(RenderInitializer):

    def getInput(self):
        return self.screen.getch()

    # def drawMainMenu(self):
    #     escape = False
    #     inGame = False
    #     self.GameState = 0
    #     while escape == False:
    #         maxY, maxX = self.screen.getmaxyx()
    #         self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
    #         menuStr = "Welcome to Hangman V0.01"
    #         selectionStr = ["1. Enter Game", "2. Exit Game"]
    #         self.screen.addstr((maxY//2) - 2, (maxX//2 - (len(menuStr) // 2)), menuStr)
    #         self.screen.addstr((maxY // 2), (maxX // 2 - (len(selectionStr[0]) // 2)), selectionStr[0])
    #         self.screen.addstr((maxY // 2)+1, (maxX // 2 - (len(selectionStr[1]) // 2)), selectionStr[1])
    #         x = self.screen.getch()
    #
    #         if x == ord('1'):
    #             escape = True
    #             self.screen.erase()
    #             curses.endwin()
    #             self.GameState = 1
    #         if x == ord('2'):
    #             escape = True
    #             self.screen.erase()
    #             curses.endwin()
    #             self.GameState = 2
    #
    #         elif x == curses.KEY_RESIZE:
    #             self.screen.erase()
    #
    # def drawObject(self, X, Y, Object):
    #     self.screen.addstr(Y,X, Object)





