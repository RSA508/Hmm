import pygame
import os

# Update with GUI elements in the future
# Move all these back to states.py?
class GenericMenu():
    def __init__(self) -> None:
        self.options = None
    

    def process_event(self,event,keybinds=None):
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) in keybinds["forward"]:
                self.loc += 1
                self.loc = self.loc % len(self.options)

            if pygame.key.name(event.key) in keybinds["backward"]:
                self.loc -= 1
                self.loc = self.loc % len(self.options)
            print(self.loc)

class MainMenu(GenericMenu):
    def __init__(self) -> None:
        super().__init__()
        self.options = ["New Game", "Load Game", "Settings", "Exit"]
        self.loc = 0

    def draw(self,surface: pygame.Surface):
        surface.fill((0,0,0))
        width,height = surface.get_rect()[2:]
        # print(height)
        font = pygame.font.SysFont(None, 50)
        # Just hardcode some cursor values for testing's sake
        pygame.draw.rect(surface, (255,255,255),(width / 2 - 350 / 2, height / 5 - 50 / 2 + self.loc * height / 5, 350, 50))
        for i, option in enumerate(self.options):
            text = font.render(option, False, (120, 240, 60))
            text_rect = text.get_rect(center=(width / 2, height / 5  * (1 + i)))
            surface.blit(text,text_rect)

class Settings(GenericMenu):
    pass


class Inventory(GenericMenu):
    pass 


class Credits(GenericMenu):
    print("""# Programming: Prathik
    # Writing: Prathik
    # Music: Prathik
    # Art: Prathik
    # Producer: Rahul
    # Director: Abhishek
    # Special thanks to Dhruv and Patricio for their moral support.
    # Without Dhruv's constant rejections and Patricio's incessant hating, this project would never be successful""")