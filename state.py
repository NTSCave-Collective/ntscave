import dill
import CONSTANTS
import random

class State():
    def __init__(self):
        self.fps = 0

        self.running = True
        self.gameOver = False
        validTile = False
        while not validTile:
            randY = random.randint(0, len(CONSTANTS.MAP))
            randX = random.randint(0, len(CONSTANTS.MAP[0]))
            try:
                if "floor" in CONSTANTS.MAP[randY][randX]:
                    self.x = randX * CONSTANTS.PIXELS + 32
                    self.y = randY * CONSTANTS.PIXELS + 32
                    validTile = True
            except:
                pass
        self.vel = CONSTANTS.PLAYER_SPEED
        self.frame = 0

        self.level = 1

        self.last_hit = CONSTANTS.TICK
        self.hearts = 5
        
        self.attack = 1
        self.attacking = False
        self.attackframe = None
        self.hit_grace = None
        self.crit = 0.1

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down

        self.enemies = list()
        self.animations = list()
        self.effects = list()
        self.activeEffects = list()

        self.newLevel = False
        self.newLevel_frame = None
        self.newLevelWidth = False

        # Define hitbox dimensions
        self.hitbox_width = CONSTANTS.PIXELS/2
        self.hitbox_height = CONSTANTS.PIXELS *3/4
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height

        # Initialize hitbox position based on enemy position
        self.update_hitbox_position()

    def update_hitbox_position(self):
        # Update hitbox position based on enemy position
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height

    def resetVars(self):
        self.fps = 0

        del CONSTANTS.MAP
        CONSTANTS.MAP = CONSTANTS.BACKGROUND_IMAGES
        self.running = False
        self.gameOver = False
        validTile = False
        while not validTile:
            randY = random.randint(0, len(CONSTANTS.MAP))
            randX = random.randint(0, len(CONSTANTS.MAP[0]))
            try:
                if "floor" in CONSTANTS.MAP[randY][randX]:
                    self.x = randX * CONSTANTS.PIXELS + 32
                    self.y = randY * CONSTANTS.PIXELS + 32
                    validTile = True
            except:
                pass
        self.vel = CONSTANTS.PLAYER_SPEED
        self.frame = 0

        self.level = 1

        self.last_hit = CONSTANTS.TICK
        self.hearts = 5
        
        self.attack = 1
        self.attacking = False
        self.attackframe = None
        self.hit_grace = None
        self.crit = 0.1

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down

        del self.enemies
        self.enemies = list()
        del self.animations
        self.animations = list()
        del self.effects
        self.effects = list()
        del self.activeEffects
        self.activeEffects = list()

        self.newLevel = False
        self.newLevel_frame = None
        self.newLevelWidth = False

        # Define hitbox dimensions
        self.hitbox_width = CONSTANTS.PIXELS/2
        self.hitbox_height = CONSTANTS.PIXELS *3/4
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height

        # Initialize hitbox position based on enemy position
        self.update_hitbox_position()

        self.moving = False
        self.clock = pygame.time.Clock()

        CONSTANTS.WORM_COUNTER = 0
        CONSTANTS.TROJAN_COUNTER = 0
        CONSTANTS.VIRUS_COUNTER = 0

        #CONSTANTS.
        CONSTANTS.roomHeight = 12
        CONSTANTS.roomWidth = 12
        CONSTANTS.PLAYER_SPEED = 5
        CONSTANTS.ATTACKDISTANCE = CONSTANTS.PIXELS
        CONSTANTS.MAP = CONSTANTS.BACKGROUND_IMAGES

def save(state):
    dill.dump(state, file = open("save.ntsc", "wb"))
    dill.dump(CONSTANTS.MAP, file = open("map.ntsc", "wb"))
    print("saved")

def load():
    new_state = State()
    new_state = dill.load(open("save.ntsc", "rb"))
    CONSTANTS.MAP = dill.load(open("map.ntsc", "rb"))
    return new_state