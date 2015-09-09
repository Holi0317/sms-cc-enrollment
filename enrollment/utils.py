#!/usr/bin/env python3
# LICENSE: MIT


import os

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
