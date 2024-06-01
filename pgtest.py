# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen_width, screen_height = pygame.display.get_surface().get_size()
clock = pygame.time.Clock()
running = True
dt = 0

class Toolbar:
    def __init__(self, width, height): #And other customisation options
        self.image = pygame.Surface((width, height))
        self.image.fill("grey")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        # self.leftbutton = ButtonClass(args)
        # self.rightbutton = ButtonClass(args)

    def update(self):
        self.leftbutton.hover() #to animate an effect if the mouse hovers over
        self.rightbutton.hover()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.leftbutton.draw(), self.leftbutton.getRect())
        screen.blit(self.rightbutton.draw(), self.rightbutton.getRect())

    def click(pos):
        if self.leftbutton.getRect().collidepoint(pos):
            self.leftbutton.click()

        if self.rightbutton.getRect().collidepoint(pos):
            self.rightbutton.click()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
toolbar = Toolbar(1280, 80)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    pygame.draw.circle(screen, "red", player_pos, 40)
    toolbar.update()
    toolbar.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()