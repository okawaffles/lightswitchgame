import pygame
from gamePartsPlayer import Player

# Platforms you can touch and gravity does not affect you. You cannot jump if you aren't touching a platform.
class Platform:
    def __init__(self, x, y, w, h, state: int) -> None:
        self.base = pygame.Rect(x,y,w,h);
        self.state = state
        self.color = 'a'
        
    def draw(self, screen: pygame.surface, groups: dict) -> None:
        if self.state == 0:
            self.color = pygame.Color(0,0,0) # black
        elif self.state == 1:
            self.color = pygame.Color(255,255,255) # white
        pygame.draw.rect(screen, self.color, self.base)

    def updateState(self, state) -> None:
        self.state = state

    def getRect(self) -> pygame.rect:
        return self.base


# Walls bounce you back if you hit them.
# They behave mostly the same as Platforms, though.
class Wall():
    def __init__(self, x, y, w, h, state: int) -> None:
        self.base = pygame.Rect(x,y,w,h)
        self.state = state
        self.color = "placeholder"

    def draw(self, screen: pygame.surface, groups: dict) -> None:
        if self.state == 0:
            self.color = pygame.Color(0,0,0)
        elif self.state == 1:
            self.color = pygame.Color(255,255,255)
        else:
            self.color = pygame.Color(100, 100, 100)
        pygame.draw.rect(screen, self.color, self.base)

    def updateState(self, state) -> None:
        self.state = state

    def getRect(self) -> pygame.rect:
        return self.base


# This is a simple class helping out with drawing text.
class Text():
    # adding equals makes the arguments not required
    def __init__(self, text: str, x: int, y: int, state: int, isGuiElement: bool = False, forcedTextSize: int = 24) -> None:
        if isGuiElement and forcedTextSize == 24:
            self.font = pygame.font.Font('assets/font.ttf', 32)
        elif isGuiElement and not forcedTextSize == 24:
            self.font = pygame.font.Font('assets/font.ttf', forcedTextSize)
        else:
            self.font = pygame.font.Font('assets/font.ttf', forcedTextSize)
        self.text = text
        self.state = state
        self.x = x
        self.y = y
        self.gui = isGuiElement
        pass

    def draw(self, screen: pygame.surface, groups: dict) -> None:
        if self.state == 0:
            self.textObj = self.font.render(self.text, True, pygame.Color(0, 0, 0))
        elif self.state == 1:
            self.textObj = self.font.render(self.text, True, pygame.Color(255, 255, 255))

        r = self.textObj.get_rect()
        r.x = self.x
        r.y = self.y

        screen.blit(self.textObj, r)


# the player must touch this to move on to the next level
class GoalPoint():
    def __init__(self, x,y,w,h) -> None:
        self.base = pygame.Rect(x,y,w,h)
        pass

    def draw(self, screen: pygame.surface, groups: dict) -> None:
        green = pygame.Color(49, 214, 101)
        pygame.draw.rect(screen, green, self.base)
        pass

    def getRect(self) -> pygame.Rect:
        return self.base


class Button():
    def __init__(self, x,y,w,h, controlsGroup: int) -> None:
        self.base = pygame.Rect(x,y,w,h)
        self.cg = controlsGroup
        self.activated = False
        pass

    def draw(self, screen: pygame.surface, groups: dict) -> None:
        blue = pygame.Color(3, 36, 252, 150)
        green = pygame.Color(49, 214, 101, 150)
        if self.activated == False:
            pygame.draw.rect(screen, blue, self.base)
        else:
            pygame.draw.rect(screen, green, self.base)
        pass

    def getRect(self) -> pygame.Rect:
        return self.base

    def checkCollision(self, player: Player) -> bool:
        try:
            if self.base.colliderect(player.getRect()):
                self.activated = True
                return True
            else: 
                return False
        except Exception as err:
            print(f'(debug) (gamePartsPlatformer/Button/checkCollision) Error: {err}')
            return False

    def getData(self) -> dict:
        return {
            'controls':self.cg,
            'activated':self.activated
        }

class ImageObject():
    def __init__(self, path, x, y, w, h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.imagePath = path
        self.image = pygame.image.load(path)
        pass

    def draw(self, screen, groups: dict) -> None:
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        screen.blit(self.image, (self.x, self.y))
        pass

# catch if the user starts the wrong file
print("""
<!> HEY!
<!> You're running the wrong file! 
<!> Run main.py to start the game!
<!> Do not delete this file as it contains critical parts of the game!
<?> If you are running main.py, this message will disappear momentarily.
""")