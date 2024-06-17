import pygame
import os
import time

class State():
    def __init__(self) -> None:
        self.finish = False
        self.previous_state = None

    def process_event(self):
        pass


class Combat(State):
    pass


class Explore(State):
    pass


class Dialogue(State):
    pass


class Menu(State):
    def __init__(self,menu) -> None:
        super().__init__()
        self.menu = menu
        # Todo
        # We want to pass a type of menu from menus.py
        # Implement methods in menu object and call from it instead of writing it here
        # print("New state")

    def process_event(self,event: pygame.Event,keybinds=None):
        # return super().process_event()
        self.menu.process_event(event,keybinds)

    def draw(self,surface: pygame.Surface):
        self.menu.draw(surface)
        pass


class Title(State):
    
    def __init__(self) -> None:
        super().__init__()
        print(self.finish)
        self.title_screen = pygame.image.load(os.getcwd() + "/../graphics/artworks-000556587030-8fjyfp-t500x500.jpg").convert()
        self.title_font = pygame.font.SysFont(None, 50)
        self.intro_font = pygame.font.SysFont(None, 50)
        self.show_text = True
        self.flicker_text = pygame.event.custom_type()
        pygame.time.set_timer(self.flicker_text, 300)

    def process_event(self,event: pygame.Event,keybinds=None):
        # for event in pygame.event.get():
        if event.type == self.flicker_text:
            self.show_text = not self.show_text
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            time.sleep(0.2)
            self.finish = True
        if event.type == pygame.VIDEORESIZE:
            width,height = event.size
            self.title_screen = pygame.transform.scale(self.title_screen,(width,height))

    def draw(self,surface: pygame.Surface):
        # blit the titlescreen image
        width,height = surface.get_rect()[2:] # To center the text properly and scale the title screen image to the actual surface size
        self.title_screen = pygame.transform.scale(self.title_screen,(width,height))
        surface.blit(self.title_screen,(0,0))
        title_text = self.title_font.render("GAME", False, (120, 240, 60))
        title_text_rect = title_text.get_rect(center=(width / 2, height / 4))
        surface.blit(title_text,title_text_rect)

        intro_text = self.intro_font.render("Press Any Key", False, (120, 240, 60))
        intro_text_rect = intro_text.get_rect(center=(width / 2, height / 2))
        self.intro_font.set_point_size(30)
        self.intro_font.set_bold(True)
        if self.show_text:
            surface.blit(intro_text,intro_text_rect)

        def update(self):
            pass


