#!/usr/bin/env python3
# LICENSE: MIT

import time
import random
import signal

from .termcolor import cprint

from . import init, utils
from .glo import obj


def troll(command):
    cmd = command.lower()
    if cmd.startswith('eval'):
        print('eval is eval.')
        return True
    elif command == 'I, the lord of python. Command you to fade in /dev/null':
        print('Aye. My Lord.')
        exit(0)
    else:
        return False


def show_question(question):
    """
    Make given question to be the selected one.

    @param (init.Question) question: question
    """
    attempt = 1
    while attempt <= obj['config']['max_attempt']:
        print('Question: ', question.question)

        if attempt > 1 and question.hint:
            print('Hint: ', question.hint)

        given = utils.input_('>>> ')

        if question.is_correct(given):
            cprint('Correct', 'green')
            time.sleep(2)
            return
        elif obj['config']['troll'] and troll(given):
            pass
        else:
            attempt += 1

    print('You have reached maximum attempt. :(')
    time.sleep(2)


def cli():
    """
    Entry point for this Application
    """
    def handler(*args, **kwargs):
        pass
    signal.signal(signal.SIGTSTP, handler)
    init.init()
    print()
    while True:
        try:
            show_question(random.choice(obj['questions']))
            utils.clear()
        except KeyboardInterrupt:
            utils.clear()
