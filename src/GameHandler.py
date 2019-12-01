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




    def setCurrentWord(self, Word):
        self.word = Word.lower()
        self.wordList = list(self.word)
        self.WordLength = len(Word)
        if self.WordLength > 10:
            raise ValueError("Word Length cannot be longer than 10")
        self.unanswered = list(" _ " * self.WordLength)


    def damagePlayer(self):
        if self.difficulty == 1:
            self.health -= 2
        elif self.difficulty == 2:
            self.health -= 4
        elif self.difficulty == 3:
            self.health -= 7
        elif self.difficulty == 4:
            self.health -= 14
        if self.health < 0:
            self.health = 0

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








