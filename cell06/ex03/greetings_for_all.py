#!/usr/bin/env python3

def greetings(txt = None):
    statestr = isinstance(txt , str)
    stateint = isinstance(txt , int)
    if (statestr):
        print(f'Hello, {txt}')
    elif (stateint):
        print(f'Error! It was not a name.')
    else :
        print(f'Hello, noble stranger.')
        
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)