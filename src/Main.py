import curses
import os
import DrawHandler
SYSTEM_EXIT = -1
draw = DrawHandler.Draw()
draw.drawMainMenu()
if(draw.GameState == 1):
    draw.drawGame()
elif(draw.GameState == 2):
    exit(SYSTEM_EXIT)
