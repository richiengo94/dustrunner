import pygame

class Button:
    def __init__(self, x: int, y: int, image: str, scale: int) -> None:
        button_image = pygame.image.load(image).convert_alpha()
        width = button_image.get_width()
        height = button_image.get_height()

        self.image = pygame.transform.scale(button_image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def set_image(self, image: str) -> None:
        button_image = pygame.image.load(image).convert_alpha()
        width = button_image.get_width()
        height = button_image.get_height()

        self.image = pygame.transform.scale(button_image, (int(width * scale), int(height * scale)))