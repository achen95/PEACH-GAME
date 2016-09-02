import pygame


class GameOver:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Story Mode")
        self.font = pygame.font.SysFont("Helvetica", 22, bold=True,
                                        italic=False)
        self.completed = False
        self.mode = "Story"
        self.background = pygame.image.load("gameover.jpeg")

    def displayMessage(self):
        gameOverMsg = "Sorry! Game over. Please try again."
        gameOverSurface = self.font.render(gameOverMsg, True, (255, 105, 180))
        self.screen.blit(gameOverSurface, (143, 350))

        continueMsg = "Press Q to continue to the main menu"
        continueSurface = self.font.render(continueMsg, True, (255, 255, 255))
        self.screen.blit(continueSurface, (130, 380))

    def runGameOver(self):
        while not self.completed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.completed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.completed = True
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, -41))

            self.displayMessage()

            pygame.display.update()
