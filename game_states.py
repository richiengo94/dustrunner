import pygame, sys, button

SCREENWIDTH, SCREENHEIGHT = 1920, 1080
FPS = 60

class GameStates:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.game_state_manager = GameStateManager('start_menu')
        self.start_menu_state = StartMenuState(self.screen, self.game_state_manager)
        self.vehicle_parts_selection_state = VehiclePartsSelectionState(self.screen, self.game_state_manager)
        self.gameplay_state = GameplayState(self.screen, self.game_state_manager)
        self.game_over_state = GameOverState(self.screen, self.game_state_manager)
        self.victory_state = VictoryState(self.screen, self.game_state_manager)
        self.pause_menu_state = PauseMenuState(self.screen, self.game_state_manager)
        self.quit_game_state = QuitGameState(self.screen, self.game_state_manager)

        self.states = {'start_menu': self.start_menu_state,
                       'vehicle_parts_selection': self.vehicle_parts_selection_state,
                       'gameplay': self.gameplay_state,
                       'game_over': self.game_over_state,
                       'victory': self.victory_state,
                       'pause_menu': self.pause_menu_state,
                       'quit_game': self.quit_game_state}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.game_state_manager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

    
class GameStateManager:
    def __init__(self, current_state: str) -> None:
        self.current_state = current_state

    def get_state(self) -> str:
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state

class StartMenuState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time * FPS)
        self.start_button: button = button.Button(200, 400, "sprites/start.png", 3)

    def run(self):
        self.display.fill('blue')
        self.start_button.draw(self.display)
        pressed = pygame.key.get_pressed()
        up, down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        if not self.key_buffer:
            if(down):
                self.game_state_manager.set_state('vehicle_parts_selection')

        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

class VehiclePartsSelectionState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time * FPS)

    def run(self):
        self.display.fill('red')
        pressed = pygame.key.get_pressed()
        up, down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        if not self.key_buffer:
            if(up):
                self.game_state_manager.set_state('start_menu')
            if(down):
                self.game_state_manager.set_state('gameplay')

        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

class GameplayState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time * FPS)

    def run(self):
        self.display.fill('orange')
        pressed = pygame.key.get_pressed()
        up, down, left, right = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)]
        if not self.key_buffer:
            if(up):
                self.game_state_manager.set_state('vehicle_parts_selection')
            if(right):
                self.game_state_manager.set_state('game_over')
            if(left):
                self.game_state_manager.set_state('victory')
            if(down):
                self.game_state_manager.set_state('pause_menu')

        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

class GameOverState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time* FPS)

    def run(self):
        self.display.fill('purple')
        pressed = pygame.key.get_pressed()
        up, down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        if not self.key_buffer:
            if(up):
                self.game_state_manager.set_state('gameplay')

        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

class VictoryState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time * FPS)

    def run(self):
        self.display.fill('green')
        pressed = pygame.key.get_pressed()
        up, down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        if not self.key_buffer:
            if(up):
                self.game_state_manager.set_state('gameplay')

        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

class PauseMenuState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time * FPS)

    def run(self):
        self.display.fill('aquamarine')
        pressed = pygame.key.get_pressed()
        up, down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        if not self.key_buffer:
            if(up):
                self.game_state_manager.set_state('gameplay')
            if(down):
                self.game_state_manager.set_state('quit_game')

        
        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

class QuitGameState:
    def __init__(self, display, game_state_manager: GameStateManager) -> None:
        self.buffer_time = 0.1
        self.display = display
        self.game_state_manager = game_state_manager
        self.key_buffer: int = int(self.buffer_time * FPS)

    def run(self):
        self.display.fill('yellow')
        pressed = pygame.key.get_pressed()
        up, down = [pressed[key] for key in (pygame.K_UP, pygame.K_DOWN)]
        if not self.key_buffer:
            if(up):
                self.game_state_manager.set_state('pause_menu')
            if(down):
                self.game_state_manager.set_state('start_menu')

        
        if self.key_buffer > 0:
            self.key_buffer -= 1
        elif self.key_buffer <= 0:
            self.key_buffer = int(self.buffer_time * FPS)

game = GameStates()
game.run()