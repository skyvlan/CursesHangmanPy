import curses
from curses import textpad
import os
import GameHandler
import time
R = 0
WR = 1
PAIR_HIGHLIGHT = 2

class RenderInitializer:

    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(PAIR_HIGHLIGHT, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(1)
        self.gamespeed = 1000 #default Framerate
        self.yBorder, self.xBorder = self.screen.getmaxyx()

    def erase(self):
        time.sleep(1 / self.gamespeed)
        self.screen.clear()
    def refresh(self):
        time.sleep(1/self.gamespeed)
        self.screen.refresh()
    def updateFrame(self):
        time.sleep(1 / self.gamespeed)
        self.screen.refresh()
        self.screen.clear()
    def EndWindow(self):
        curses.endwin()


class RenderObject(RenderInitializer):

    def drawBorder(self, Refresh=R):
        if Refresh == R:
            self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
            time.sleep(1 / self.gamespeed)
            self.screen.refresh()
        elif Refresh == WR:
            self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
        else:
            raise(ValueError, "Only WR and R are allowed")

    def drawObject(self, Xpos, Ypos, Text, Refresh=R):
        if Refresh == R:
            self.screen.addstr(Ypos, Xpos, Text)
            time.sleep(1 / self.gamespeed)
            self.screen.refresh()
        elif Refresh == WR:
            self.screen.addstr(Ypos, Xpos, Text)
        else:
            raise(ValueError, "Only WR and R are allowed")

    def enableColor(self, COL, Refresh=R):
        if Refresh == R:
            self.screen.attron(curses.color_pair(COL))
            time.sleep(1 / self.gamespeed)
            self.screen.refresh()
        elif Refresh == WR:
            self.screen.attron(curses.color_pair(COL))
        else:
            raise (ValueError, "Only WR and R are allowed")

    def disableColor(self, COL, Refresh=R):
        if Refresh == R:
            self.screen.attroff(curses.color_pair(COL))
            time.sleep(1 / self.gamespeed)
            self.screen.refresh()
        elif Refresh == WR:
            self.screen.attroff(curses.color_pair(COL))
        else:
            raise (ValueError, "Only WR and R are allowed")

    def drawRect(self, X, Y, Width, Length, Refresh=R):
        if Refresh == R:
            textpad.rectangle(self.screen, Y, X, Y + Length, X + Width)
            time.sleep(1 / self.gamespeed)
            self.screen.refresh()
        elif Refresh == WR:
            textpad.rectangle(self.screen, Y, X, Y + Length, X + Width)
        else:
            raise (ValueError, "Only WR and R are allowed")

class InputHandler(RenderInitializer):

    def getInput(self):
        return self.screen.getch()

    def getStringInput(self,x,y): # please call curses.echo() before calling
        string = self.screen.getstr(y,x,10) #max length of string is 16
        return string



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





