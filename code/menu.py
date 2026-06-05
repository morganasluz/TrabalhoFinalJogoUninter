#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.examples.grid import WINDOW_WIDTH
from pygame.font import Font
from pygame import Surface, Rect

from code.Const import WIN_WIDTH, MENU_OPTION, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.Bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True: #carrega as músicas e faz looping infinito da imagem inicial
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Winter", 65, (138, 43, 226), ((WIN_WIDTH / 2), 70))
            self.menu_text("Combat", 65, (138, 43, 226), ((WIN_WIDTH / 2), 130))

            for i in range(len(MENU_OPTION)):
                self.menu_text(MENU_OPTION[i], 20, COLOR_BLACK, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            # checar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close window
                    quit() #end pygame

    def menu_text(self, text: str, text_size: int,  text_color: tuple, text_center_pos):
        text_font: Font = pygame.font.SysFont(name= "Georgia", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



