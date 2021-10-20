class Car_Class:
    def __init__(self, display_height, x_change, left_pic, center_pic, right_pic):
        self.x = 210
        self.x_change = x_change
        self.y = display_height * 0.8
        self.x_target = self.x
        self.left_blit = left_pic
        self.center_blit = center_pic
        self.right_blit = right_pic
        self.x_move = 0
        self.leniency = 2.7
        self.current = center_pic
        self.map = self.current.map

    def right(self):
        if self.x_target != 310:
            self.x_target += self.x_change

    def left(self):
        if self.x_target != 10:
            self.x_target -= self.x_change

    # TODO Fix the collision system
    def update(self, speed):
        self.x_move = speed / 2
        if self.x_target - self.leniency < self.x < self.x_target + self.leniency:
            self.x = self.x_target
        if self.x_target < self.x:
            self.x -= self.x_move
            self.left_blit.blit(self.x, self.y)
            self.current = self.left_blit
        elif self.x_target > self.x:
            self.x += self.x_move
            self.right_blit.blit(self.x, self.y)
            self.current = self.right_blit
        else:
            self.center_blit.blit(self.x, self.y)
            self.current = self.center_blit
        self.map = self.current.map
