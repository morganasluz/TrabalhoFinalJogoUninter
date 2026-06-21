#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, MENU_OPTION
from code.level import Level
from code.menu import Menu

class Game:
    def __init__(self, WIN_HEIGHT=None):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))  # janela inicial

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() #fecha janela
                quit() #fim de jogo
            else:
                pass


