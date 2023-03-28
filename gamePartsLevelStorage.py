# Here is where the levels are stored.
# The levels are stored as object data in a dictionary inside a class.
# This allows for easy data access

from gamePartsPlatformer import Platform, Wall, Text, Button, ImageObject, DeathObject

class Levels():
    def __init__(self) -> None:
        # DECOR = always drawn regardless of state or conditionals
        # WHITE = collide state 1
        # BLACK = collide state 0
        # SPAWN = indicates where the player should start out
        # GOAL  = indicates where the goal point should be placed
        # SETUP = settings to change what the player can do
        self.levels = {
            # This "level" uses every object to test if they're working
            # well, it did before i neglected it
            'TEST':{
                'DECOR':[
                    Text("test level", 5, 5, 1),
                ],
                'WHITE':{
                    'platforms':[
                        Platform(20, 70, 40, 10, 1),
                        Platform(60, 90, 40, 10, 1),
                        Platform(100, 110, 40, 10, 1),
                    ],
                    'walls':[
                        #Wall(60, 40, 10, 40, 1),
                    ]
                },
                'BLACK':{
                    'platforms':[
                        Platform(20, 170, 40, 10, 0),
                        Platform(60, 190, 40, 10, 0),
                        Platform(100, 210, 40, 10, 0),
                    ],
                    'walls':[
                        Wall(60, 140, 10, 40, 0),
                    ]
                },
                "BUTTONS":[

                ],
                'GOAL':{
                    'x':250,
                    'y':250,
                    'w':25,
                    'h':25
                }
            },

            # Level one
            1:{
                'SETUP':{
                    'canFlip':False,
                    'hasNextLevel':True,
                    'usesGroups':False
                },
                'DECOR':[
                    Text("press the left and right arrow to move", 8, 5, 1),
                    Text("get to the green platform to move on.", 8, 37, 1)
                ],
                'WHITE':{
                    'platforms':[
                        Platform(0, 270, 600, 10, 1),
                        Platform(40, 320, 600, 10, 1),
                    ],
                    'walls':[
                        Wall(-10, 0, 10, 480, 1),
                        Wall(640, 0, 10, 480, 1)
                    ]
                },
                'BLACK':{
                    'platforms':[],
                    'walls':[]
                },
                'GOAL':{
                    'x':0,
                    'y':320,
                    'w':40,
                    'h':10
                },
                "BUTTONS":[

                ],
                'SPAWN':[
                    50, 200
                ]
            },

            # level two
            2:{
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':False
                },
                'DECOR':[
                    Text("press space to flip your state", 8, 5, 1),
                    Text("black passes through black,", 8, 37, 1),
                    Text("white passes through white,", 8, 69, 1),
                    Text("you can't pass through grey.", 8, 101, 1),

                    ImageObject('./assets/coconut.jpg', 100, 200, 50, 50),
                    Text("this is a coconut", 8, 250, 1)
                ],
                'WHITE':{
                    'platforms':[
                        Platform(500-65, 50, 140, 10, 1),
                        Platform(500-65, 250, 140, 10, 1),
                    ],
                    'walls':[
                        Wall(500-75, 0, 10, 480, 3), # state 3 is used to draw the walls in grey
                        Wall(500+75, 0, 10, 480, 3)
                    ]
                },
                'BLACK':{
                    'platforms':[
                        Platform(500-65, 150, 140, 10, 0),
                        Platform(500-65, 350, 140, 10, 0),
                    ],
                    'walls':[
                        Wall(500-75, 0, 10, 480, 3),
                        Wall(500+75, 0, 10, 480, 3)
                    ]
                },
                "BUTTONS":[

                ],
                'GOAL':{
                    'x':500-65,
                    'y':430,
                    'w':140,
                    'h':10
                },
                'SPAWN':[
                    500, 0
                ]
            },
            
            # Level Three
            3: {
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':False
                },
                'DECOR':[
                    Text("press up arrow to jump", 8, 5, 1),
                    Text("get to the green to move on.", 8, 37, 1)
                ],
                'WHITE':{
                    'platforms':[
                        Platform(5, 240, 50, 10, 1),
                        Platform(105, 240, 50, 10, 1),
                        Platform(205, 240, 50, 10, 1),
                        Platform(305, 240, 50, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[],
                    'walls':[]
                },
                "BUTTONS":[

                ],
                'GOAL':{
                    'x':405,
                    'y':240,
                    'w':50,
                    'h':10
                },
                'SPAWN':[
                    20, 200
                ]
            },

            # Level Four
            4: {
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':False
                },
                'DECOR':[
                    Text("try jumping and switching at the same time", 8, 5, 1),
                    Text("get to the green to move on.", 8, 37, 1)
                ],
                'WHITE':{
                    'platforms':[
                        Platform(5, 240, 50, 10, 1),
                        Platform(205, 240, 50, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[
                        Platform(105, 240, 50, 10, 0),
                        Platform(305, 240, 50, 10, 0),
                    ],
                    'walls':[]
                },
                "BUTTONS":[

                ],
                'GOAL':{
                    'x':405,
                    'y':240,
                    'w':50,
                    'h':10
                },
                'SPAWN':[
                    20, 200
                ]
            },

            # Level Five
            5: {
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':True
                },
                'DECOR':[
                    Text("sometimes, you need to click buttons to move on.", 8, 5, 1),
                    Text("try pushing the button.", 8, 37, 1)
                ],
                'WHITE':{
                    'platforms':[
                        Platform(5, 240, 50, 10, 1),
                        Platform(205, 240, 50, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[
                        Platform(105, 240, 50, 10, 0),
                        Platform(305, 240, 50, 10, 0),
                    ],
                    'walls':[]
                },
                "BUTTONS":[
                    Button(310, 235, 40, 5, 1),
                ],
                'GOAL':{
                    'x':5,
                    'y':240,
                    'w':50,
                    'h':10,
                    'group':1
                },
                'SPAWN':[
                    20, 200
                ]
            },

            # Level Six
            6: {
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':True
                },
                'DECOR':[
                    Text("i really like buttons", 8, 5, 1),
                    Text("push them all. now.", 8, 37, 1)
                ],
                'WHITE':{
                    'platforms':[
                        # a half white platform in the center
                        Platform(100, 240, 220, 10, 1),
                        # some higher platforms
                        Platform(350, 210, 50, 10, 1),
                        Platform(400, 180, 50, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[
                        # a half black platform in the center
                        Platform(320, 240, 220, 10, 0),
                        # some higher platforms
                        Platform(250, 210, 50, 10, 0),
                        Platform(200, 180, 50, 10, 0),
                    ],
                    'walls':[]
                },
                "BUTTONS":[
                    Button(300, 235, 40, 5, 1),
                    # these buttons will appear after each other are pressed
                    Button(205, 175, 40, 5, 2, 1),
                    Button(405, 175, 40, 5, 3, 2),
                    Button(255, 205, 40, 5, 4, 3),
                ],
                'GOAL':{
                    'x':5,
                    'y':240,
                    'w':50,
                    'h':10,
                    'group':4
                },
                'SPAWN':[
                    150, 100
                ]
            },

            # Level Seven
            7: {
                'SETUP':{
                    'canFlip':False,
                    'hasNextLevel':True,
                    'usesGroups':False
                },
                'DECOR':[
                    Text("whatever you do, do not touch red.", 8, 5, 1),
                    Text("you will die.", 8, 37, 1),
                ],
                'WHITE':{
                    'platforms':[
                        # a half white platform in the center
                        Platform(25, 200, 125, 10, 1),
                        Platform(175, 200, 50, 10, 1),
                        Platform(250, 200, 50, 10, 1),
                        Platform(325, 200, 50, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[
                        
                    ],
                    'walls':[]
                },
                "BUTTONS":[
                    
                ],
                'DEATHOBJECTS':[
                    # die
                    DeathObject(150, 205, 25, 5),
                    DeathObject(225, 205, 25, 5),
                    DeathObject(300, 205, 25, 5),
                    DeathObject(375, 205, 25, 5),
                ],
                'GOAL':{
                    'x':400,
                    'y':200,
                    'w':50,
                    'h':10
                },
                'SPAWN':[
                    75, 100
                ]
            },

            # Level Eight
            8: {
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':False,
                    'usesCustomGroupSet':True,
                    'currentLevelGroups':[ # allow for five button groups
                        False, False, False, False, False
                    ]
                },
                'DECOR':[
                    Text("this is a reverse button", 8, 5, 1),
                    Text("it will remove an object from the level.", 8, 37, 1),
                ],
                'WHITE':{
                    'platforms':[
                        # a half white platform in the center
                        Platform(25, 300, 590, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[
                        
                    ],
                    'walls':[]
                },
                "BUTTONS":[
                    Button(125, 295, 35, 5, 1, -1, True)
                ],
                'DEATHOBJECTS':[
                    # die
                    DeathObject(315, 100, 10, 200, 1),
                ],
                'GOAL':{
                    'x':400,
                    'y':300,
                    'w':50,
                    'h':10
                },
                'SPAWN':[
                    50, 200
                ]
            },

            # Level Nine
            9: {
                'SETUP':{
                    'canFlip':True,
                    'hasNextLevel':True,
                    'usesGroups':False,
                    'usesCustomGroupSet':False,
                    'currentLevelGroups':[]
                },
                'DECOR':[
                    Text("make your way to the goal.", 8, 5, 1),
                    Text("good luck!", 8, 37, 1),
                ],
                'WHITE':{
                    'platforms':[
                        Platform(0, 175, 200, 10, 1),
                        Platform(0, 105, 50, 10, 1),
                        Platform(70, 105, 50, 10, 1),

                        Platform(300, 235, 50, 10, 1),
                        Platform(300, 165, 50, 10, 1),
                    ],
                    'walls':[]
                },
                'BLACK':{
                    'platforms':[
                        Platform(0, 140, 50, 10, 0),
                        Platform(50, 235, 200, 10, 0),

                        Platform(300, 200, 50, 10, 0),
                    ],
                    'walls':[]
                },
                "BUTTONS":[
                    Button(75, 100, 40, 5, 1, -1, True),
                    Button(55, 230, 40, 5, 2, -1, True),
                ],
                'DEATHOBJECTS':[
                    # group -1
                    DeathObject(0, 185, 200, 5, -1),
                    # group 1
                    DeathObject(200, 35, 10, 150, 1),
                ],
                'GOAL':{
                    'x':400,
                    'y':300,
                    'w':50,
                    'h':10
                },
                'SPAWN':[
                    100, 90
                ]
            }
        }
        pass

    # Get the level dictionary that the user needs.
    def get(self, key) -> dict:
        return self.levels[key]



# catch if the user starts the wrong file
print("""
<!> HEY!
<!> You're running the wrong file! 
<!> Run main.py to start the game!
<!> Do not delete this file as it contains critical parts of the game!
<?> If you are running main.py, this message will disappear momentarily.
""")