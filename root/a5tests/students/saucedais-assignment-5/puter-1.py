#!/usr/bin/env python3
'''
Author: <Isaiah Sauceda>
Date: <2/23/17>
Class: CSC 250
Description:
<This program will mimic a small query and response engine.>
'''
from datetime import datetime

#---------------------------------Functions------------------------------------
def color_switch(x):
    '''
    This function acts as a switch statement and computes color.
    The x parameter is the number of times the question has been asked.
    This function returns the color choices.
    '''
    return {
        0 : 'red!',
        1 : 'blue!',
        2 : 'green!'
    }.get(x,None)
    
def run_puter():
    '''
    This function will answer questions entered by the user.
    This function accepts no parameters.
    This function prints responses to certain queries.
    '''
    qn = 0
    count = 0
    
    while qn < 10:
        qu = input("PUTER: Go ahead, ask me something: ").lower()
        
        if qu == 'how are you?' or qu == 'how goes it?':
            print("PUTER: I am a computer program, so obviously I am excellent!")
            qn += 1
        
        elif qu == 'what is your birthday?':
            print("PUTER: I am a computer program! I don't have a birthday :-(")
            qn += 1
            
        elif qu == 'what is your favorite color?':
            print(color_switch(count))
            if count < 2:
                count += 1
            else:
                count = 0
            qn += 1
        
        elif qu == 'what time is it?' or qu == 'what is the date?':
            print('PUTER: The current date/time is ' + str(datetime.now()))
            qn += 1
        
        elif qu == 'exit':
            print('PUTER: Bye!')
            break
        
        else:
            print('Sorry, I can\'t understand you!')
            qn += 1
        
    print("PUTER: Question limit reached. Bye!")
    
#==========================================================
def main():
    '''
    Testing was be done here. Trust me
    '''
    print("PUTER: Hello and welcome! Ask me no more than 10 questions.")
    run_puter()
    
if __name__ == '__main__':
    main()