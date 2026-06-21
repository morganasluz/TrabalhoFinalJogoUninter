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
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]:
                pygame.quit() #fecha janela
                quit() #fim de jogo
            else:
                pass


