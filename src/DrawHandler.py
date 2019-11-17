import curses
import os
import GameHandler

class Draw:

    def __init__(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.highlightText = curses.color_pair(1)
        self.normalText = curses.A_NORMAL

        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(1)

    def drawMainMenu(self):
        escape = False
        inGame = False
        self.GameState = 0
        while escape == False:
            maxY, maxX = self.screen.getmaxyx()
            self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
            menuStr = "Welcome to Hangman V0.01"
            selectionStr = ["1. Enter Game", "2. Exit Game"]
            self.screen.addstr((maxY//2) - 2, (maxX//2 - (len(menuStr) // 2)), menuStr)
            self.screen.addstr((maxY // 2), (maxX // 2 - (len(selectionStr[0]) // 2)), selectionStr[0])
            self.screen.addstr((maxY // 2)+1, (maxX // 2 - (len(selectionStr[1]) // 2)), selectionStr[1])
            x = self.screen.getch()

            if x == ord('1'):
                escape = True
                self.screen.erase()
                curses.endwin()
                self.GameState = 1
            if x == ord('2'):
                escape = True
                self.screen.erase()
                curses.endwin()
                self.GameState = 2

            elif x == curses.KEY_RESIZE:
                self.screen.erase()


    def drawGame(self):
        escape = False
        inGame = False
        self.GameState = 0
        Game = GameHandler.Game()
        while escape == False:
            maxY, maxX = self.screen.getmaxyx()
            self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
            menuStr = "Game State"

            self.screen.addstr(2,2, menuStr)
            self.screen.addstr(8, 2, Game.hangman[0])
            x = self.screen.getch()

            if x == ord('1'):
                escape = True
                self.screen.erase()
                curses.endwin()
                self.GameState = 1


            if x == ord('2'):
                escape = True
                self.screen.erase()
                curses.endwin()
                self.GameState = 2


            elif x == curses.KEY_RESIZE:
                self.screen.erase()



