import pygame
import MiniGameMode
import StoryMode


class WelcomeScreen:
    def __init__(self):
        # initializes pygame
        pygame.init()
        # loads music to play infinitely (until stop)
        pygame.mixer.music.load('Overworld.ogg')
        pygame.mixer.music.play(-1)
        # Screen size (x, y)
        self.screenSize = (640, 480)
        # displays the screen of the screen size
        self.screen = pygame.display.set_mode(self.screenSize)
        # initializes the font type
        self.font = pygame.font.SysFont("Helvetica", 18, bold=False,
                                        italic=False)
        # Sets window title
        pygame.display.set_caption("Welcome To Super Princess Peach!")
        # Variable the continues or stops game loop
        self.completed = False

    def runStoryMode(self):
        # makes an instance of the sprite class, peach
        #  sets initial coordinates at (20, 355)
        storyMode = StoryMode.StoryMode(20, 355)
        # allows loop to run with peach sprite
        storyMode.runStoryMode(storyMode)

    def runMiniGameMode(self):
        miniGameMenu = MiniGameMode.MiniGameMode()
        miniGameMenu.runMiniGameMenu()

    def displayMessage(self):
        # draws rect for "Press S for story mode"
        # (where to put rectangle, (color), (width, height, x, y)
        pygame.draw.rect(self.screen, (255, 130, 180), (410, 70, 195, 30))
        # draws rect for M for mini game mode
        pygame.draw.rect(self.screen, (255, 130, 180), (390, 120, 245, 30))

        # Writes message onto rectangle
        storyMsg = "Press S for Story Mode"
        # (text, makes letter smoother (anti alias), color)
        storyMsgSurface = self.font.render(storyMsg, True, (0, 0, 0))
        # Puts message onto screen at the points (x, y)
        # (starting at top left corner)
        self.screen.blit(storyMsgSurface, (415, 75))

        miniMsg = "Press M for Mini Game Mode"
        miniMsgSurface = self.font.render(miniMsg, True, (0, 0, 0))
        # this draws a source surface onto another surface (screen)
        # surface.blit(source surface, (top-left corner coordinates of source))
        self.screen.blit(miniMsgSurface, (395, 125))

        quitMsg = "Press Q to quit program"
        quitMsgSurface = self.font.render(quitMsg, True, (0, 0, 0))
        self.screen.blit(quitMsgSurface, (5, 5))

    def renderHomeScreen(self):
        # Loads the castle background
        homeScreen = pygame.image.load("PeachCastle2.png")
        # Scales it to size of screen ((width, height)
        homeScreen = pygame.transform.scale(homeScreen, (640, 480))
        # Puts it onto screen, top left corner is at the points (0, 0)
        self.screen.blit(homeScreen, (0, 0))

        # loads the peach logo and scales it down to correct size
        peachSign = pygame.image.load("super_princess_peach_logo.gif")
        peachSign = pygame.transform.scale(peachSign, (290, 100))
        self.screen.blit(peachSign, (5, 50))

        # loads the peach image and scales it down to correct size
        peachImg = pygame.image.load("peach.png")
        peachImg = pygame.transform.scale(peachImg, (120, 200))
        self.screen.blit(peachImg, (50, 280))

        # loads the mario image and scales it down to correct size
        marioImg = pygame.image.load("mario2.png")
        marioImg = pygame.transform.scale(marioImg, (120, 200))
        self.screen.blit(marioImg, (500, 280))

    def runWelcomeScreen(self):
        # Game loop
        # While self.completed == False
        while not self.completed:
            # Gets the user input because it is an event drivn GUI
            for event in pygame.event.get():
                # If the user quits game by clicking
                # the 'X' in the corner of screen
                if event.type == pygame.QUIT:
                    # reassigns self.completed and terminates loop
                    self.completed = True
                # If a key is pressed
                if event.type == pygame.KEYDOWN:
                    # If the m is pressed "Mini Game" function is called
                    if event.key == pygame.K_m:
                        self.runMiniGameMode()
                    # If the s is pressed "Story Mode" function is called
                    if event.key == pygame.K_s:
                        self.runStoryMode()
                    # If q is pressed, program is exited by reassigning
                    # self.completed to True and terminating loop
                    if event.key == pygame.K_q:
                        self.completed = True

            # Calls each function
            self.renderHomeScreen()
            self.displayMessage()

            # Updates screen with each iteration in the while loop
            pygame.display.update()
