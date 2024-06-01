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


# initialization
# toolbar = Toolbar(1280, 80)

# animate
# toolbar.update()
# toolbar.draw(screen)