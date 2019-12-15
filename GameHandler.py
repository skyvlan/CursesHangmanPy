import curses
import GameEngine
import random

class Game():

    def __init__(self):
        self.hangman = [
            "",

            """
               _________
                |/        
                |              
                |                
                |                 
                |               
                |                   
                |___                 
                """,

            """
               _________
                |/   |      
                |              
                |                
                |                 
                |               
                |                   
                |___                 
                H""",

            """
               _________       
                |/   |              
                |   (_)
                |                         
                |                       
                |                         
                |                          
                |___                       
                HA""",

            """
               ________               
                |/   |                   
                |   (_)                  
                |    |                     
                |    |                    
                |                           
                |                            
                |___                    
                HAN""",

            """
               _________             
                |/   |               
                |   (_)                   
                |   /|                     
                |    |                    
                |                        
                |                          
                |___                          
                HANG""",

            """
               _________              
                |/   |                     
                |   (_)                     
                |   /|\                    
                |    |                       
                |                             
                |                            
                |___                          
                HANGM""",

            """
               ________                   
                |/   |                         
                |   (_)                      
                |   /|\                             
                |    |                          
                |   /                            
                |                                  
                |___                              
                HANGMA""",

            """
               ________
                |/   |     
                |   (_)    
                |   /|\           
                |    |        
                |   / \        
                |               
                |___           
                HANGMAN"""]

        self.health = 14
        self.difficulty = 1 #Default (Easy) = 1, Medium = 2, Hard = 3, Hardcore = 4
        self.hangmanState = 0
        self.score = 0



    def setCurrentWord(self, Word):
        self.word = Word.lower()
        self.wordList = list(self.word)
        self.WordLength = len(Word)
        if self.WordLength > 16:
            raise ValueError("Word Length cannot be longer than 16")
        self.unanswered = list("_" * self.WordLength)


    def damagePlayer(self):
        self.health -= 2

        if self.health == 14:
            self.hangmanState = 0
        if self.health < 14:
            self.hangmanState = 1
        if self.health < 12:
            self.hangmanState = 2
        if self.health < 10:
            self.hangmanState = 3
        if self.health < 8:
            self.hangmanState = 4
        if self.health < 6:
            self.hangmanState = 5
        if self.health < 4:
            self.hangmanState = 6
        if self.health < 2:
            self.hangmanState = 7
        if self.health == 0:
            self.hangmanState = 8
    def checkifAnswerCorrect(self):
        if self.wordList == self.unanswered:
            return True
        else:
            return False


def splitletter(word):
    tmp = []
    for i in word:
            try:
                ind = tmp.index(i)
            except:
                tmp.append(i)
    return tmp







