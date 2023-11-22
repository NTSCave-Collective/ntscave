import random
import numpy as np



def generateRoom():
    roomHeight = 12
    roomWidth = 12

    room = [[0 for _ in range(roomWidth)] for _ in range(roomHeight)]


    #######################################################################################################################
    ## SOURCE: https://medium.com/@yvanscher/cellular-automata-how-to-create-realistic-worlds-for-your-game-2a9ec35f5ba9 ##
    #######################################################################################################################

    shape = (roomWidth, roomHeight)
    WALL = 0
    FLOOR = 1

    # set the probability of filling
    # a wall at 40% not 50%
    fill_prob = 0.4

    new_map = np.ones(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            choice = random.uniform(0, 1)
            # replace 0.5 with fill_prob
            new_map[i, j] = WALL if choice < fill_prob else FLOOR

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
            # WIP: PUT CORRECT WALL

            # CORNERS
            if i == 0 and j == 0:
                room[0][0] = "wallcorner_topleft"
            elif i == 0 and j == roomWidth - 1:
                room[0][j] = "wallcorner_topright"
            elif i == roomHeight - 1 and j == 0:
                room[i][0] = "wallcorner_bottomleft"
            elif i == roomHeight - 1 and j == roomWidth - 1:
                room[i][j] = "wallcorner_bottomright"

            # outside walls
            elif j == 0:
                room[i][0] = "wall_left"
            elif j == roomWidth - 1:
                room[i][roomWidth - 1] = "wall_right"
            elif i == 0:
                room[0][j] = random.choices(["frontwall_center", "frontwall_left", "frontwall_right"], weights=(50, 25, 25), k=1)[0]
            
            else:
                room[i][j] = random.choices(["floor", "floor2", "floor3"], weights=(10,10,10), k=1)[0]


    return room



# new_map[new_map == 0.0] = "frontwall_center"
# new_map[new_map == 1.0] = "frontwall_center"


# strings = ["%.2f" % number for number in new_map]

# print(new_map)

# print(room)







# def makeNoiseGrid(density):
#     noiseGrid = [[0 for x in range(roomWidth)] for y in range(roomHeight)]

#     for i in range(len(noiseGrid)):
#         for j in range(len(noiseGrid[i])):
#             randomNr = random.randint(1, 100)
#             if randomNr > density:
#                 noiseGrid[i][j] = 0     # floor
#             else:
#                 noiseGrid[i][j] = 1     # wall
#     return noiseGrid

# def applyCellularAutomaton(grid, iterations):
#     for i in range(iterations):
#         temp_grid = grid
#         for j in range(roomHeight):
#             for k in range(roomWidth):
#                 neighborWallCount = 0
#                 neighborMatrix = neighbors(grid, 1, k, j)
#                 # print(neighborMatrix)
#                         # if(y != j or x != k): #ignore current tile
#                             # neighborWallCount += 1
#                 if neighborWallCount > 4:
#                     grid[j][k] = 1 # wall
#                 else:
#                     grid[j][k] = 0 # floor

#     return grid
                        

# def neighbors(a, radius, row_number, column_number):
#      return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
#                 for j in range(column_number-1-radius, column_number+radius)]
#                     for i in range(row_number-1-radius, row_number+radius)]

# noiseMatrix = makeNoiseGrid(45)
# applyCellularAutomaton(noiseMatrix, 5)





# minWallDistance = 8
# maxWallDistance = 14

# def generateRoom():
#     wallDistance = random.randint(minWallDistance, maxWallDistance)
#     randomOffsetL = random.randint(0,2)
#     randomOffsetR = random.randint(0,2)

#     for i in range(randomOffsetL):
#         room[0].append(None)
    
#     prev = None

#     for i in range(wallDistance):
#         if i == 0:
#             room[0].append("wallcorner_topleft")
#         elif i == wallDistance - 1:
#             room[0].append("wallcorner_topright")
#         else:
#             if room[0][i - 1] == "frontwall_left":
#                 room[0].append(random.choice(["frontwall_center", "frontwall_left"]))
#             elif room[0][i - 1] == "frontwall_right":
#                 room[0].append(random.choice(["frontwall_center", "frontwall_right"]))
#             else:
#                 room[0].append(random.choices(["frontwall_center", "frontwall_left", "frontwall_right"], weights=(50, 25, 25), k=1)[0])
                    
#     for i in range(randomOffsetR):
#         room[0].append(None)
    
#     # print(room)


# generateRoom()
