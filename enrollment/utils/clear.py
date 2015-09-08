#!/usr/bin/env python3
# LICENSE: MIT


import os


def clear():
    """
    Clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
