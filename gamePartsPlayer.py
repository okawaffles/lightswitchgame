import pygame

class Player():
    # called when the object is created
    def __init__(self) -> None:
        self.x = 50
        self.y = 50
        #self.base = pygame.Rect(self.x - 10, self.y - 10, 20, 20) # player is 20x20 square
        self.state = 1 # 0 = black, 1 = white
        self.xBounceDir = 0
        self.yBounceDir = 0
    
    # self explanitory function
    def draw(self, screen: pygame.surface) -> None:
        # update the player object each draw
        self.base = pygame.Rect(self.x - 10, self.y - 10, 20, 20)
        # draw an outline!
        self.outline = pygame.Rect(self.x - 11, self.y - 11, 22, 22)
        if self.state == 0:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), self.outline)
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), self.base)
        elif self.state == 1:
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), self.outline)
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), self.base)

    # also self explanitory function
    def setPosition(self, x, y) -> None:
        self.x = x
        self.y = y

    # update the position, don't set it.
    def updatePosition(self, x, y) -> None:
        self.x += x
        self.y += y
        if x < 0:
            self.xBounceDir = -1
        elif x > 0:
            self.xBounceDir = 1
        if y < 0:
            self.yBounceDir = -1
        elif y > 0:
            self.yBounceDir = 1 

    # return the position of the player as a dictionary
    def getPosition(self) -> dict:
        return {'x':self.x,'y':self.y}

    # set the state of the "lightswitch" (black or white)
    def setState(self, state) -> None:
        self.state = state

    # this checks if the player collides with the provided rect
    def collides(self, check: pygame.rect, wall: bool = False) -> bool:
        if self.base.colliderect(check) and wall:
            if self.xBounceDir == -1:
                print('(debug) wall bouncing right.')
                self.x += 3
            elif self.xBounceDir == 1:
                self.x -= 3
                print('(debug) wall bouncing left.')
            if self.yBounceDir == -1:
                self.y += 3
                print('(debug) wall bouncing down.')
            elif self.yBounceDir == 1:
                self.y -= 3
                print('(debug) wall bouncing up.')
            self.xBounceDir = 0
            self.yBounceDir = 0
        
        return self.base.colliderect(check)

    def getRect(self) -> pygame.rect:
        return self.base



# catch if the user starts the wrong file
print("""
<!> HEY!
<!> You're running the wrong file! 
<!> Run main.py to start the game!
<!> Do not delete this file as it contains critical parts of the game!
<?> If you are running main.py, this message will disappear momentarily.
""")