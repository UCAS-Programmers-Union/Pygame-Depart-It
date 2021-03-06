import pygame

import GameStates.GameClasses.game_classes as gc
import color as clr

class State():
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

class MenuState(State):
    def __init__(self):
        super().__init__()

        # TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
        # of just Windows.

        # TODO: Find a way to download/package a font so that this can be done
        # without having to load images and can be blitted normally with text.
        self.one_player_text = pygame.image.load(r'src\GameStates\text_for_1p.jpg')
        self.two_player_text = pygame.image.load(r'src\GameStates\text_for_2p.jpg')
        self.instructions_text = pygame.image.load(r'src\GameStates\text_for_instructions.jpg')

        # Rescale images to better fit the window.
        self.one_player_text = pygame.transform.scale(self.one_player_text, (292, 25))
        self.two_player_text = pygame.transform.scale(self.two_player_text, (307, 25))
        self.instructions_text = pygame.transform.scale(self.instructions_text, (474, 24))

        self.wall_sprites_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()

        self._load_map()
        self._create_map()

    # I have to create a separate load file as GameMaze.maze is not designed to load start-menu.txt. 
    def _load_map(self):
        # TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
        # of just Windows.
        with open('src\GameStates\start_menu.txt', 'r') as opened_file:
            self.raw_map_file = opened_file.read()

        self.raw_map_file = self.raw_map_file.splitlines()

        self.temp_map_list = []
        self.map_list = []

        for row in self.raw_map_file:
            for character in row:
                self.temp_map_list.append(character)
            
            self.map_list.append(self.temp_map_list)
            self.temp_map_list = []

    def _create_map(self):
        for y_index in range(len(self.map_list)):
            for x_index in range(len(self.map_list[y_index])):
                if self.map_list[y_index][x_index] == "X":
                    self.wall_block = gc.WallBlock(x_index, y_index)
                    
                    self.wall_sprites_group.add(self.wall_block)
                    self.all_sprites_group.add(self.wall_block)

    ## Core Function
    def render(self, display):
        display.fill(clr.BLACK)

        self.all_sprites_group.draw(display)

        # TODO: Find a way to use the screen's display width and height to calculate
        # the placement of the text instead of manually changing and adding it.
        # TODO: Center and align text correctly.
        display.blit(self.one_player_text, (80, 320))
        display.blit(self.two_player_text, (400, 320))
        display.blit(self.instructions_text, (160, 400))
    ##

    ## Core Function
    def update(self):
        pass
    ##

    ## Core Function
    def event_handling(self, pressed_buttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if pressed_buttons[pygame.K_RETURN]:
                # TODO: Switch the game_state to OnePlayerGameState
                pygame.quit()
                quit()
            elif pressed_buttons[pygame.K_SPACE]:
                # TODO: Switch the game_state to TwoPlayerGameState
                pygame.quit()
                quit()
            elif pressed_buttons[pygame.K_i]:
                # TODO: Switch the game_state to InstructionState
                pygame.quit()
                quit()
    ##