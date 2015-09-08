#!/usr/bin/env python3
# LICENSE: MIT


import os


def clear():
    """
    Clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def input_(text=''):
    """
    Input function that will not exit until it sees a response.
    """
    while True:
        try:
            thing = input(text)
            if thing == '':
                raise ValueError
            else:
                return thing
        except (EOFError, KeyboardInterrupt, ValueError):
            print()
