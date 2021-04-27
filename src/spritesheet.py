import pygame


class Spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    # Load a specific image from a specific rectangle

    def image_at(self, rectangle):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image


class Spritesheet2(object):
    def __init__(self, filename, width, height, max_img_num=None):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.width = width
        self.height = height

        if max_img_num is not None:
            self.max_img_num = max_img_num
        else:
            self.max_img_num = (self.sheet.get_width()/self.width) * (self.sheet.get_height()/self.height)

        assert self.sheet.get_width() % self.width == 0
        assert self.sheet.get_height() % self.height == 0

        # Load a specific image from a specific rectangle

    def image_at(self, rectangle):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def get_image(self, img_num):
        '''
        Returns the nth image in the spritesheet
        :param img_num: number image in spritesheet
        :type img_num: int
        :return:
        '''
        print("getting image")
        chosen_img = self.image_at((img_num*self.width, img_num*self.height, self.width, self.height))

        return chosen_img # type: pygame.Surface