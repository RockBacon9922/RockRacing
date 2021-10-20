class RoadClass():
    def __init__(self, i, type):
        """
        Init's The pygame surface
        :param i: the identification of the road
        """
        self.i = i
        self.x = 400
        self.y = 116
        self.type = type
        self.posy = self.y * self.i
        self.reset_height = -116

    def move(self, speed, display_height):
        if self.posy >= display_height + 55:
            self.posy = self.reset_height
        else:
            self.posy += speed