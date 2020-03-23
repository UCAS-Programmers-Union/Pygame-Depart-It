import pygame

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

    # TODO: Find a way to download/package a font so that this can be done
    # without having to load images and can be blitted normally with text.
    self.one_player_text = pygame.image.load('text_for_1p.jpg')
    self.two_player_text = pygame.image.load('text_for_2.jpg')
    self.instructions_text = pygame.image.load('text_for_instructions')

    ## Core Function
    def render(self, screen):
        screen.fill(clr.BLACK)

        # TODO: Find a way to use the screen's display width and height to calculate
        # the placement of the text instead of manually changing and adding it.
        # TODO: Center and align text correctly.
        screen.blit(self.one_player_text, (80, 340))
        screen.blit(self.two_player_text, (400, 340))
        screen.blit(self.instructions_text, (160, 420))
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

            if pressed_buttons[K_SPACE]:
                # TODO: Switch this to the game state.
                pygame.quit()
                quit()
    ##