#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH
from code.menu import Menu

class Game:
    def __init__(self, WIN_HEIGHT=None):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))  # janela inicial

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
