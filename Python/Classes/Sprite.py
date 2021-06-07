"""Program by William Stoneham 2020"""
class Sprite:
    def __init__(self, Image1, Image2):
        self.pic = Image1
        self.pic2 = Image2
        self.size = (self.pic.x, self.pic.y)
        self.x = -self.pic.x
        self.y = -self.pic.y
        self.map = self.pic.map
        self.current = self.pic

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def update(self, type):
        if type:
            self.pic2.blit(self.x, self.y)
        else:
            self.pic.blit(self.x, self.y)