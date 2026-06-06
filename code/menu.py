#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame import Surface, Rect

from const import WIN_WIDTH, MENU_OPTION, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.Bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True: #carrega as músicas e faz looping infinito da imagem inicial
            #imagem e textos
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Winter", 65, (138, 43, 226), ((WIN_WIDTH / 2), 70))
            self.menu_text("Combat", 65, (138, 43, 226), ((WIN_WIDTH / 2), 130))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(MENU_OPTION[i], 20, (255, 255, 0), ((WIN_WIDTH / 2), 200 + 25 * i))

                else:
                    self.menu_text(MENU_OPTION[i], 20, COLOR_BLACK, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()


            #eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #close window
                    quit() #end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #tecla para baixo
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: #tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: #enter e retorna
                        return MENU_OPTION[menu_option]


    def menu_text(self, text: str, text_size: int,  text_color: tuple, text_center_pos):
        text_font: Font = pygame.font.SysFont(name= "Georgia", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



