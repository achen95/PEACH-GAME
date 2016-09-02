import pygame


class SpriteSheet:
    def __init__(self, filename):
        # opens the file if it exists
        # .convert() is used to convert the pygame surface (screen) to the same
        # pixel format as the surface used for final display (image)
        try:
            self.spriteSheet = pygame.image.load(filename).convert()
        except pygame.error:
            print("Unable to load sprite sheet image", filename)
            raise SystemExit

    # loads a specific image from rectangle in sheet
    def image_at(self, rectangle, colorkey=None):
        # Loads image from x,y,x+offset,y+offset
        # this sets the rectangular coordinates of the sprite as rect
        rect = pygame.Rect(rectangle)
        # this sets the specific part of the spreadsheet as it's own variable
        # must convert to make the pixel format of spreadsheet same as image
        image = pygame.Surface(rect.size).convert(self.spriteSheet)
        image.blit(self.spriteSheet, (0, 0), rect)
        # this makes the image transparent or with a color background if
        # colorkey is given
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
