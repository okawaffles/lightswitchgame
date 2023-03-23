import os
try:
    # attempt to import pygame
    import pygame
except:
    # attempt to install pygame and re-import it
    os.system("pip install pygame")
    try:
        import pygame
    except:
        print("Tried to install pygame, but failed. Please install pygame.")
        sys.exit(-1)

import sys, time, math

try:
    from gamePartsPlatformer import Platform, Wall, Text, GoalPoint
    from gamePartsPlayer import Player
    from gamePartsLevelStorage import Levels
except:
    print("You are missing critical components. Please make sure that gamePartsPlatformer.py, gamePartsLevelStorage.py, gamePartsPlayer.py, and the assets folder are all present in the same directory as main.py");
    sys.exit(-1)

# clear out any "running the wrong file" warning messages.
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou are running the correct file.")

try:
    pygame.image.load(os.path.join('assets', 'coconut.jpg'))
except:
    print("You are missing coconut.jpg. I told you it was important.")
    sys.exit(-1);

# set up pygame
pygame.init()

# set up pygame's window
winSize = width, height = 640, 480
showTitleScreen = True
pygame.display.set_caption("lightswitch")
fullscreenOn = False
main = 0
screen = 0

if fullscreenOn:
    # fullscreen is never used.
    screen = pygame.Surface(winSize)
    main = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(winSize)

# 3/4 of these aren't even used. but here's some basic colors.
colors = {
    "red":pygame.Color(255,0,0),
    "green":pygame.Color(0,255,0),
    "blue":pygame.Color(0,0,255),
    "white":pygame.Color(255, 255, 255),
    "black":pygame.Color(0,0,0),
    "darkgrey":pygame.Color(24, 24, 24),
    "lightgrey":pygame.Color(64, 64, 64),
}

# create our main variables
player = Player()
state = 0 # 0 = black, 1 = white
player.setState(state)
player_vel_y = 0  # vertical velocity
gravity = 0.5  # force of gravity
max_vel_y = 10  # maximum vertical velocity
collides = False
levels = Levels()
levelId = 7
groupEnabled = 0 # i dont know if this is required
currentLevel = levels.get(levelId)
currentLevelGroups = [ # allow for five button groups
    False, False, False, False, False
]
hearts = 3
# set the start point
player.updatePosition(currentLevel['SPAWN'][0], currentLevel['SPAWN'][1])
g_escapeFrames = 0

while True:
    for event in pygame.event.get():
        # check if the player wants to quit
        if event.type == pygame.QUIT: sys.exit()

        # check jump and swap keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and collides:
                # set our variables so the player jumps (experiences reverse velocity)
                player_vel_y = -5
                player.updatePosition(0, -10)
            if event.key == pygame.K_SPACE and currentLevel['SETUP']['canFlip']:
                # switch the state!
                if state == 0:
                    state = 1
                else:
                    state = 0
                # switches between black and white states
                player.setState(state)
            if event.key == pygame.K_p:
                levelId += 1
                currentLevel = levels.get(levelId)
            if event.key == pygame.K_r:
                hearts = 0

    # switch the background color of the screen based on state
    if state == 0:
        screen.fill(colors["darkgrey"])
    elif state == 1:
        screen.fill(colors["lightgrey"])
    
    # get the held keys for movement.
    keys = pygame.key.get_pressed() #checking pressed keys
    if keys[pygame.K_LEFT]:
        player.updatePosition(-3, 0)
    if keys[pygame.K_RIGHT]:
        player.updatePosition(3, 0)
    if keys[pygame.K_ESCAPE]:
        print(f"(debug) HTE key [ESC] held | {g_escapeFrames} / 30")
        g_escapeFrames += 1
        Text(f"EXIT... {round((g_escapeFrames/30) * 100)}%", 3, 410, 1, False).draw(screen, {})
        if g_escapeFrames > 30:
            sys.exit()
    else:
        Text(f"HOLD ESC TO EXIT", 3, 410, 1, False).draw(screen, {})
        g_escapeFrames = 0

    
    # draw our level's objects
    for p in currentLevel["WHITE"]['platforms']:
        p.draw(screen, currentLevelGroups)
    for p in currentLevel["BLACK"]['platforms']:
        p.draw(screen, currentLevelGroups)
    for w in currentLevel["WHITE"]['walls']:
        w.draw(screen, currentLevelGroups)
    for w in currentLevel["BLACK"]['walls']:
        w.draw(screen, currentLevelGroups)
    for d in currentLevel["DECOR"]:
        d.draw(screen, currentLevelGroups)
    # check if the player is touching a button
    # try makes it optional to have in the level config (i added it afterwards)
    try:
        for b in currentLevel["BUTTONS"]:
            b.draw(screen, currentLevelGroups)
            b.checkCollision(player)
            # update groups if button pushed
            buttonData = b.getData()
            currentLevelGroups[buttonData["controls"]] = buttonData["activated"]
    except Exception as e:
        print(f"(debug) caught exception! {e}")
        pass
    # draw our goalpoint
    goalData = currentLevel["GOAL"]
    goalPoint = GoalPoint(goalData['x'],goalData['y'],goalData['w'],goalData['h'])
    if not currentLevel["SETUP"]["usesGroups"]:
        goalPoint.draw(screen, currentLevelGroups)
    else:
        if currentLevelGroups[goalData['group']]:
            goalPoint.draw(screen, currentLevelGroups)
    
    player.draw(screen)

    # check if player is touching ground
    collides = False
    if state == 0:
        for p in currentLevel["WHITE"]['platforms']:
            # we do a very specific calculation to try and make sure that the player 
            # doesn't go through the platform if their velocity is too high
            if(player.collides(p.getRect()) and p.getRect().y < player.getPosition()['y'] + 10):
                collides = True
                player_vel_y = 0
                # check if the player is below the platform
                # if {player bottom is below bottom} and {player top is above bottom} 
                if (player.getRect().bottom > p.getRect().bottom and player.getRect().top < p.getRect().bottom):
                    print('(debug) Player is touching bottom of platform')
                    # check if player has velocity, if its up or none, push them down. if its downward, push them up
                    if (player_vel_y <= 0):
                        player.updatePosition(0, 5)
                    else:
                        player.updatePosition(0, -5)
    else:
        for p in currentLevel["BLACK"]['platforms']:
            if(player.collides(p.getRect()) and p.getRect().y < player.getPosition()['y'] + 10):
                collides = True
                player_vel_y = 0
                if (player.getRect().bottom > p.getRect().bottom and player.getRect().top < p.getRect().bottom):
                    print('(debug) Player is touching bottom of platform')
                    # check if player has velocity, if its up or none, push them down. if its downward, push them up
                    if (player_vel_y <= 0):
                        player.updatePosition(0, 5)
                    else:
                        player.updatePosition(0, -5)

    
    # this checks wall collision. walls are special because they bounce the player back
    # rather then preventing gravity and allowing jumping.
    for w in currentLevel["WHITE"]['walls']:
        player.collides(w.getRect(), True)
    for w in currentLevel["BLACK"]['walls']:
        player.collides(w.getRect(), True)

    # update the player's velocity if they don't collide.
    if (not collides):
        player.updatePosition(0, player_vel_y)
        player_vel_y += gravity
    else:
        player_vel_y = 0

    # check if the player is touching the goal
    if player.collides(goalPoint.getRect(), False) and currentLevel['SETUP']['hasNextLevel']:
        # probably could fit this in above statement. checks if the groups subsystem is enabled and the goal's group is enabled (via button)
        if currentLevel["SETUP"]["usesGroups"]:
            if currentLevelGroups[currentLevel["GOAL"]["group"]]:
                # load the next level
                levelId += 1
                try:
                    currentLevel = levels.get(levelId)
                    player.setPosition(currentLevel['SPAWN'][0], currentLevel['SPAWN'][1])
                except KeyError as err:
                    print("(debug) Error whilst loading next level (level does not exist)\n(debug) The game cannot continue.")
                    sys.exit()
                except Exception as err:
                    print(f"(debug) Error whilst loading next level (generic: {err})\n(debug) The game cannot continue.")
                    sys.exit()
                player.setState(0)
                state = 0
                player_vel_y = 0
        # (groups subsystem is not loaded)
        else:
            # load the next level
            levelId += 1
            try:
                currentLevel = levels.get(levelId)
                player.setPosition(currentLevel['SPAWN'][0], currentLevel['SPAWN'][1])
            except KeyError as err:
                print("(debug) Error whilst loading next level (level does not exist)\n(debug) The game cannot continue.")
                sys.exit()
            except Exception as err:
                print(f"(debug) Error whilst loading next level (generic: {err})\n(debug) The game cannot continue.")
                sys.exit()
            player.setState(0)
            state = 0
            player_vel_y = 0

    # check if the player is offscreen on the bottom
    if player.getPosition()['y'] > 480:
        player.setPosition(currentLevel['SPAWN'][0], currentLevel['SPAWN'][1])
        player.setState(0)
        state = 0
        hearts -= 1
        currentLevelGroups = [False,False,False,False,False]

    # GUI elements
    guilives = Text("Lives:", 2, 430, 1, False).draw(screen, {})
    if hearts == 3:
        guihearts = Text("Œ Œ Œ", 5, 450, 1, True).draw(screen, {}) # OE symbol shows up as full heart in this font.
    elif hearts == 2:
        guihearts = Text("Œ Œ §", 5, 450, 1, True).draw(screen, {}) # § symbol shows up as empty heart in this font.
    elif hearts == 1:
        guihearts = Text("Œ § §", 5, 450, 1, True).draw(screen, {})
    else:
        guihearts = Text("§ § §", 5, 450, 1, True).draw(screen, {})

    # IMPORTANT: blit the current frame so we can actually see it
    # this expands the screen to be fullscreen
    if fullscreenOn:
        screen_transformed = pygame.transform.scale(screen, (1440, 1080))
        main.blit(screen_transformed, (240, 0)) # rect 240,0 moves it to the center of the screen
        # updates the screen so we can see!
        pygame.display.flip()
    else:
        pygame.display.flip()

    # gameover logic
    if hearts <= 0:
        for i in range(60):
            screen.fill(colors["darkgrey"])
            Text("§ § §", 5, 450, 1, True).draw(screen, {})
            pygame.display.flip()
            time.sleep(1/60)
        hearts = 4 # important since we kill the player later
        levelId = 1
        currentLevel = levels.get(levelId)
        currentLevelGroups = [False,False,False,False,False]

        # show gameover screen
        for i in range(180):
            Text("Game Over", 210, 150, 1, True, 48).draw(screen, {})
            pygame.display.flip()
            time.sleep(1/60)

        player.updatePosition(0, 480) # kill the player to reset their spawn

    

    # keep last. locks to 60fps to prevent over-using cpu
    time.sleep(1/60)