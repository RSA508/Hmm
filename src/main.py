import pygame
import configparser
import os
import time
import states
import menus
 
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
class Game():

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(os.getcwd() + "/../data/config.ini")
        self.states = None
        self.fps = int(self.config["DISPLAY"]["FPS"])
        self.clock = pygame.time.Clock()
        self.screen_width = int(self.config["DISPLAY"]["WIDTH"])
        self.screen_height = int(self.config["DISPLAY"]["HEIGHT"])
        self.keybinds = dict([(key,self.config["CONTROLS2"][key].lower()) for key in self.config["CONTROLS2"]])
        self.actions = None
        self.is_fullscreen = False
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.surface = pygame.Surface((self.screen_width, self.screen_height)) 
        self.end_game = False
        self.state_stack = [states.Menu(menus.MainMenu()),states.Title()]
        self.state = self.state_stack[-1]
        # We create a cache needed to solve a very annoying issue with the window drifting in position everytime pygame.display.set_mode is called
        # It would be ideal to find a fix using pygame.transform.scale...
        self.display_cache = {"FPS":self.fps,"HEIGHT":self.screen_height,"WIDTH":self.screen_width}
        pygame.display.set_caption("GAME (THIS IS A PLACEHOLDER DUH)")
        for key in self.config["CONTROLS2"]:
            print(key)
        # print(self.config["CONTROLS2"]["FORWARD"])
        print(self.keybinds)

    def update_config(self):
        self.config.read(os.getcwd() + "/../data/config.ini")
        self.fps = int(self.config["DISPLAY"]["FPS"])
        self.screen_height = int(self.config["DISPLAY"]["HEIGHT"])
        self.screen_width = int(self.config["DISPLAY"]["WIDTH"])
    
    def update_state(self):
        if self.state != self.state_stack[-1]:
            self.state = self.state_stack[-1]
    
    def resize_display(self):
        if self.screen_height != self.display_cache["HEIGHT"] or self.screen_width != self.display_cache["WIDTH"]:
            self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
            self.surface = pygame.Surface((self.screen_width, self.screen_height)) 
            self.display_cache["HEIGHT"], self.display_cache["WIDTH"] = self.screen_height, self.screen_width

    def game_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.screen_width,self.screen_height = event.size
                self.resize_display()
            if event.type == pygame.QUIT:
                self.end_game = True
            self.state.process_event(event,keybinds=self.keybinds)
            self.state.draw(self.surface)
            if self.state.finish: 
                self.state_stack.pop()
            self.update_state()
            # self.state.update()
            # if event.type == pygame.KEYDOWN:
            #     if event.dict["key"] == 120:
            #         self.updateConfig()
            #         self.resizeDisplay()

    def run_game(self):
        last_time = time.time()
        while not self.end_game:
            self.window.blit(self.surface,(0,0))
            dt = time.time() - last_time
            last_time = time.time()
            self.clock.tick(self.fps)
            self.game_loop()
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.update_config()
    game.run_game()