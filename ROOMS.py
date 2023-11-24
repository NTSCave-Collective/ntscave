import random
import numpy as np
import CONSTANTS
import enemy
from math import floor
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.grid import Grid
from pathfinding.core.diagonal_movement import DiagonalMovement

def swap_map(state, map):
    if map == "random":
        valid_map = False
        global stairTile
        while not valid_map:
            generatedMap, originMap = generateRoom()
            print(generatedMap)
            floorList = list(zip(*np.where(originMap==1.0)))

            # GENERATE ROOMS
            if len(floorList) >= 12:
                isValidTile = False
                while not isValidTile:
                    stairTile = random.choice(floorList)
                    if not generatedMap[stairTile[0]][stairTile[1]] in ["wall_right", "wall_left"]:
                        generatedMap[stairTile[0]][stairTile[1]] = "stairs_down"
                        isValidTile = True
                    else:
                        continue
            else:
                continue

            npMap = np.array(generatedMap)
            spikesPos = list(zip(*np.where(npMap=="spike")))
            
            # SELECT PLAYER SPAWN POSITION
            playerStartTile = random.choice(floorList)

            matrix = np.array(originMap)
            grid = Grid(matrix=matrix)
            start = grid.node(playerStartTile[1], playerStartTile[0])
            end = grid.node(stairTile[1], stairTile[0])

            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, runs = finder.find_path(start, end, grid)

            if len(path) <= 4 or playerStartTile in spikesPos:
                continue
            else:
                state.x = playerStartTile[1] * 64 + 32
                state.y = playerStartTile[0] * 64 + 32
                CONSTANTS.MAP = generatedMap
                CONSTANTS.originMap = originMap
                valid_map = True

    else:
        CONSTANTS.MAP = map

    enemy.generate_enemies(state)
    CONSTANTS.SURFACE_WIDTH = CONSTANTS.PIXELS * len(CONSTANTS.MAP)
    CONSTANTS.SURFACE_HEIGHT = CONSTANTS.PIXELS * max([len(y) for y in CONSTANTS.MAP])
    state.newLevelWidth = True

def generateRoom():

    room = [[0 for _ in range(CONSTANTS.roomWidth)] for _ in range(CONSTANTS.roomHeight)]


    #######################################################################################################################
    ## SOURCE: https://medium.com/@yvanscher/cellular-automata-how-to-create-realistic-worlds-for-your-game-2a9ec35f5ba9 ##
    #######################################################################################################################

    shape = (CONSTANTS.roomWidth, CONSTANTS.roomHeight)
    WALL = 0
    FLOOR = 1

    # set the probability of filling
    # a wall at 40%
    fill_prob = 0.4

    new_map = np.ones(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            choice = random.uniform(0, 1)
            # replace 0.5 with fill_prob
            new_map[i, j] = WALL if choice < fill_prob else FLOOR


    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            if j == 0:
                new_map[i][0] = WALL
            elif j == CONSTANTS.roomWidth - 1:
                new_map[i][CONSTANTS.roomWidth - 1] = WALL
            elif i == 0:
                new_map[0][j] = WALL
            elif i == CONSTANTS.roomHeight - 1:
                new_map[CONSTANTS.roomHeight - 1][j] = WALL

    generations = 6
    for generation in range(generations):
        for i in range(shape[0]):
            for j in range(shape[1]):
                # get the number of walls 1 away from each index
                # get the number of walls 2 away from each index
                submap = new_map[max(i-1, 0):min(i+2, new_map.shape[0]),max(j-1, 0):min(j+2, new_map.shape[1])]
                wallcount_1away = len(np.where(submap.flatten() == WALL)[0])
                submap = new_map[max(i-2, 0):min(i+3, new_map.shape[0]),max(j-2, 0):min(j+3, new_map.shape[1])]
                wallcount_2away = len(np.where(submap.flatten() == WALL)[0])
                # this consolidates walls
                # for first five generations build a scaffolding of walls
                if generation < 5:
                    # if looking 1 away in all directions you see 5 or more walls
                    # consolidate this point into a wall, if that doesnt happpen
                    # and if looking 2 away in all directions you see less than
                    # 7 walls, add a wall, this consolidates and adds walls
                    if wallcount_1away >= 5 or wallcount_2away <= 7:
                        new_map[i][j] = WALL
                    else:
                        new_map[i][j] = FLOOR
                    if i==0 or j == 0 or i == shape[0]-1 or j == shape[1]-1:
                        new_map[i][j] = WALL 
                # this consolidates open space, fills in standalone walls,
                # after generation 5 consolidate walls and increase walking space
                # if there are more than 5 walls nearby make that point a wall,
                # otherwise add a floor
                else:
                    # if looking 1 away in all direction you see 5 walls
                    # consolidate this point into a wall,
                    if wallcount_1away >= 5:
                        new_map[i][j] = WALL
                    else:
                        new_map[i][j] = FLOOR

    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            if j == 0:
                new_map[i][0] = WALL
            elif j == CONSTANTS.roomWidth - 1:
                new_map[i][CONSTANTS.roomWidth - 1] = WALL
            elif i == 0:
                new_map[0][j] = WALL
            elif i == CONSTANTS.roomHeight - 1:
                new_map[CONSTANTS.roomHeight - 1][j] = WALL

    CONSTANTS.originMap = new_map

    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            try:
                topLeftNeighbor = new_map[i - 1][j - 1]
            except:
                topLeftNeighbor = WALL
            try:
                leftNeighbor = new_map[i][j - 1]
            except:
                leftNeighbor = WALL
            try:
                bottomLeftNeighbor = new_map[i + 1][j - 1]
            except:
                bottomLeftNeighbor = WALL
            try:
                topNeighbor = new_map[i - 1][j]
            except:
                topNeighbor = WALL
            try:
                bottomNeighbor = new_map[i + 1][j]
            except:
                bottomNeighbor = WALL
            try:
                topRightNeighbor = new_map[i - 1][j + 1]
            except:
                topRightNeighbor = WALL
            try:
                rightNeighbor = new_map[i][j + 1]
            except:
                rightNeighbor = WALL
            try:
                bottomRightNeighbor = new_map[i + 1][j + 1]
            except:
                bottomRightNeighbor = WALL
                
            
            if new_map[i][j] == WALL:
                if leftNeighbor == FLOOR and topLeftNeighbor == FLOOR and topNeighbor == FLOOR and topRightNeighbor == FLOOR and rightNeighbor == FLOOR and bottomRightNeighbor == FLOOR and bottomNeighbor == FLOOR and bottomLeftNeighbor == FLOOR:
                    room[i][j] = "wall_single"
                elif topNeighbor == FLOOR and leftNeighbor == FLOOR and rightNeighbor == FLOOR and bottomNeighbor == WALL:
                    room[i][j] = "singlewall_top_connected"
                elif topNeighbor == FLOOR and rightNeighbor == FLOOR and bottomNeighbor == FLOOR and leftNeighbor == WALL:
                    room[i][j] = "singlewall_right_connected"
                elif topNeighbor == WALL and rightNeighbor == FLOOR and bottomNeighbor == FLOOR and leftNeighbor == FLOOR:
                    room[i][j] = "singlewall_bottom_connected"
                elif topNeighbor == FLOOR and rightNeighbor == WALL and bottomNeighbor == FLOOR and leftNeighbor == FLOOR:
                    room[i][j] = "singlewall_left_connected"
                elif (topNeighbor == WALL and bottomNeighbor == FLOOR) or (topNeighbor == FLOOR and bottomNeighbor == FLOOR):
                    room[i][j] = random.choices(["frontwall_center", "frontwall_left", "frontwall_right"], weights=(80,10,10), k=1)[0]
                elif topNeighbor == FLOOR and rightNeighbor == FLOOR and bottomNeighbor == WALL:
                    room[i][j] = "wallcorner_topright"
                elif topNeighbor == FLOOR and leftNeighbor == FLOOR and bottomNeighbor == WALL:
                    room[i][j] = "wallcorner_topleft"
                elif topLeftNeighbor == FLOOR and topNeighbor == WALL and leftNeighbor == WALL and bottomNeighbor == WALL and rightNeighbor == WALL:
                    room[i][j] = "void_connection_topleft"
                elif topNeighbor == FLOOR and leftNeighbor == WALL and rightNeighbor == WALL:
                    room[i][j] = "frontwall_center"
                else:
                    room[i][j] = None

            else:
                if rightNeighbor == WALL and topRightNeighbor == WALL and bottomRightNeighbor == WALL and bottomNeighbor == WALL and bottomLeftNeighbor == WALL and topNeighbor == FLOOR and leftNeighbor == FLOOR:
                    room[i][j] = "wallcorner_bottomright"
                elif leftNeighbor == WALL and topLeftNeighbor == WALL and bottomLeftNeighbor == WALL and topNeighbor == FLOOR and bottomNeighbor == WALL and bottomRightNeighbor == WALL and topRightNeighbor == FLOOR:
                    room[i][j] = "wallcorner_bottomleft"
                elif leftNeighbor == WALL and topLeftNeighbor == WALL and bottomLeftNeighbor == WALL:
                    room[i][j] = "wall_left"
                elif rightNeighbor == WALL and topRightNeighbor == WALL and bottomRightNeighbor == WALL:
                    room[i][j] = "wall_right"
                elif bottomNeighbor == WALL and bottomRightNeighbor == WALL and bottomLeftNeighbor == WALL:
                    room[i][j] = "wall_bottom"
                else:
                    room[i][j] = random.choices(["floor", "floor2", "floor3", "spike"], weights=(60,10,30,5), k=1)[0]

    return [room, new_map]