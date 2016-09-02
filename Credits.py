import pygame


class Credits:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Credits")
        self.completed = False
        self.clock = pygame.time.Clock()
        # FPS = Frames per second
        self.FPS = 20
        # retrieves a font from system.
        # pygame.font.SysFont(name, size, bold=boolean, italic=boolean)
        self.font = pygame.font.SysFont("Helvetica", 22, bold=True,
                                        italic=False)
        self.background = pygame.image.load("peachAndFriends.png")
        self.background = pygame.transform.scale(self.background, (300, 200))

    def displayCredits(self):
        # draws a black box with white outline around congrats message
        # pygame.draw.rect(self.screen, (255, 255, 255), (175, 12, 297, 37))
        # pygame.draw.rect(self.screen, (0, 0, 0), (179, 16, 289, 29))

        congratsMsg = "Congratulations! You Won!"
        congratsSurface = self.font.render(congratsMsg, True, (255, 105, 180))
        self.screen.blit(congratsSurface, (185, 20))

        creditsMsg = "Game Created By:"
        creditsSurface = self.font.render(creditsMsg, True, (20, 170, 50))
        self.screen.blit(creditsSurface, (225, 50))

        thanksMsg = "Special thanks to all the players!"
        thanksSurface = self.font.render(thanksMsg, True, (255, 30, 0))
        self.screen.blit(thanksSurface, (160, 210))

        continueMsg = "Press Q to continue to the main menu"
        continueSurface = self.font.render(continueMsg, True, (255, 255, 255))
        self.screen.blit(continueSurface, (130, 240))

    def writeNames(self):
        samMsg = "Sam Kustin"
        adamMsg = "Adam Nieto"
        amyMsg = "Amy Chen"
        melissaMsg = "Melissa Wolff"

        samCredit = self.font.render(samMsg, True, (0, 191, 255))
        self.screen.blit(samCredit, (250, 110))

        adamCredit = self.font.render(adamMsg, True, (0, 191, 255))
        self.screen.blit(adamCredit, (250, 140))

        amyCredit = self.font.render(amyMsg, True, (0, 191, 255))
        self.screen.blit(amyCredit, (255, 80))

        melissaCredit = self.font.render(melissaMsg, True, (0, 191, 255))
        self.screen.blit(melissaCredit, (245, 170))

    def runCredits(self):
        while not self.completed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.completed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.completed = True
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (180, 280))

            self.displayCredits()
            self.writeNames()

            pygame.display.update()
