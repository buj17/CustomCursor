import os.path

import pygame

pygame.init()
_size = width, height = 400, 300
_main_screen = pygame.display.set_mode(_size)


def load_image(filename, colorkey=None) -> pygame.Surface:
    fullname = os.path.join('data', filename)
    if not os.path.isfile(fullname):
        pass
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Customcursor(pygame.sprite.Sprite):
    cursor_image = load_image('CustomCursor.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Customcursor.cursor_image
        self.rect = self.image.get_rect()

    def set_pos(self, pos: tuple[int, int]):
        self.rect.x, self.rect.y = pos


class MainWindow:
    def __init__(self):
        pygame.init()
        self.fps = 60
        self.size = _size
        self.screen = _main_screen
        self.main_sprite_group = pygame.sprite.Group()
        self.custom_cursor = Customcursor(self.main_sprite_group)

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def run(self):
        clock = pygame.time.Clock()
        running = True
        pygame.mouse.set_visible(False)

        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if pygame.mouse.get_focused():
                self.custom_cursor.set_pos(pygame.mouse.get_pos())
                self.main_sprite_group.draw(self.screen)
                self.main_sprite_group.update()
            pygame.display.flip()
            clock.tick(self.fps)
        pygame.quit()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
