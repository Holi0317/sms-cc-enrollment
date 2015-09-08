#!/usr/bin/env python3
# LICENSE: MIT

"""
Initialize this app
"""

import os
import json

from termcolor import colored, cprint

from . import utils
from .glo import obj, obj_lock

BUDDA = r'''

                                _oo8oo_
                               o8888888o
                               88" . "88
                               (| -_- |)
                               0\  =  /0
                             ___/'==='\___
                           .' \\|     |// '.
                          / \\|||  :  |||// \
                         / _||||| -:- |||||_ \
                        |   | \\\  -  /// |   |
                        | \_|  ''\---/''  |_/ |
                        \  .-\__  '-'  __/-.  /
                      ___'. .'  /--.--\  '. .'___
                   ."" '<  '.___\_<|>_/___.'  >' "".
                  | | :  `- \`.:`\ _ /`:.`/ -`  : | |
                  \  \ `-.   \_ __\ /__ _/   .-` /  /
              =====`-.____`.___ \_____/ ___.`____.-`=====
                                `=---=`


     ~~~~~~~Powered by https://github.com/ottomao/bugfreejs~~~~~~~

                        佛祖保佑         永无bug

'''

DEFAULT_CONFIG = {
    'questions': [
        {
            'question': 'foo',
            'answer': 'bar',
            'hint': 'The answer is bar',
            'ignore_case': True
        }
    ],
    'max_attempt': 3,
    'troll': True
}


class Question(object):

    def __init__(self, q):
        """
        Construct a question.

        @param (dict) q: dict object read from config.
        @return None.
        """
        for item in ('question', 'answer', 'hint', 'ignore_case'):
            if item not in q:
                raise ValueError('Item: {0} does not have key {1}.'.format(
                    q, item))

        self.question = q['question']
        self.answer = q['answer']
        self.hint = q['hint']
        self.ignore_case = q['ignore_case']

    def is_correct(self, attempt):
        """
        Is attempt correct?

        @param (str) attempt: attempted answer
        @return (bool): is attempt correct.
        """
        if self.ignore_case:
            attempt = attempt.lower()
        return self.answer == attempt


def _handle_perm_error(path):
    """
    Handle permission error by printing it out and exit

    @param (str) path: Path that cannot write into
    """
    print('Cannot write to {0}. Do you have the right permission?'.format(
        path))
    exit(1)


def _ask_make_config(path):
    """
    Ask if user wants to create config at path

    @param (str) path: path that config will be created
    """
    res = input('Do you want to create a new config file (Y/N)? ').lower()
    if res == 'y':
        make_config(path)
        with obj_lock:
            obj['config'] = DEFAULT_CONFIG
    elif res == 'n':
        print('Fix the config and come again.')
        exit(1)
    else:
        print('Invalid choice: {0}'.format(res))
        exit(1)


def make_config(path):
    """
    Create default config on given path

    @param (str) path: path to write config into
    @return None
    """
    with open(path, 'w') as file:
        file.write(json.dumps(DEFAULT_CONFIG))


def init():
    """
    Perform directory check, print ridiculous thing
    """
    utils.clear()
    cprint('Initializing...', 'blue')

    # Read config
    config_file = os.path.join(os.path.expanduser('~'), '.enrollment.json')
    if not os.path.exists(config_file):
        make_config(config_file)

    try:
        with open(config_file, 'r') as file:
            read = file.read()
    except:
        _handle_perm_error(config_file)

    try:
        with obj_lock:
            obj['config'] = json.loads(read)
    except ValueError:
        print('{0} is not valid json.')
        _ask_make_config(config_file)

    # create questions
    obj['questions'] = []
    for item in obj['config']['questions']:
        with obj_lock:
            obj['questions'].append(Question(item))

    if obj['config']['troll']:
        print('Troll is {0}. Enjoy:)'.format(colored('enabled', 'green')))
        print(BUDDA)
    else:
        print('Troll is {0}. :('.format(colored('disabled', 'red')))
    cprint('Initialization completed!', 'green')
