TILE_SIZE = 50
WIDTH = TILE_SIZE * 18
HEIGHT = TILE_SIZE * 17

tiles = ['path', 'block', 'reward', 'blue_door', 'blue_key','red_key','red_door','yellow_key','yellow_door',
    'green_key','green_door','pink_cell']
unlock = 0

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 3, 0, 1, 1, 0, 1, 11, 1, 10, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 11, 11, 1, 0, 2, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 11, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 8, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 9, 1],
    [1, 0, 1, 0, 11, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 11, 1],
    [1, 0, 0, 1, 0, 11, 5, 0, 0, 1, 0, 0, 0, 1, 1, 11, 11, 1],
    [1, 1, 0, 1, 1, 1, 11, 1, 11, 1, 0, 1, 6, 1, 1, 11, 1, 1],
    [1, 7, 0, 1, 11, 11, 11, 11, 11, 11, 0, 4, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Actor("pacman", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
ghost = Actor("devil", anchor=(1, 1), pos=(7 * TILE_SIZE, 15 * TILE_SIZE))
enemy = Actor("ghost", anchor=(0, 0), pos=(13 * TILE_SIZE, 5 * TILE_SIZE))
enemy2 = Actor("ghost3", anchor=(0, 0), pos=(14 * TILE_SIZE, 14 * TILE_SIZE))
enemy.yv = -1
ghost.yv = -1
enemy2.yv = -1
def draw():
    screen.clear()
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][column]]
            screen.blit(tile, (x, y))
    player.draw()
    enemy.draw()

def on_key_down(key):
    # player movement
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    tile = tiles[maze[row][column]]
    if tile == 'path':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(player, duration=0.1, pos=(x, y))
    global unlock
    if tile == 'reward':
        print("Winner Winner Grapes Dinner")
        exit()
    elif tile == 'blue_key':
        unlock = unlock + 1
        maze[row][column] = 0 # 0 is 'empty' tile
    elif tile == 'blue_door' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0 # 0 is 'empty' tile

    if tile == 'green_key':
        unlock = unlock + 1
        maze[row][column] = 0 # 0 is 'empty' tile
    elif tile == 'green_door' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0 # 0 is 'empty' tile

    if tile == 'red_key':
        unlock = unlock + 1
        maze[row][column] = 0 # 0 is 'empty' tile
    elif tile == 'red_door' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0 # 0 is 'empty' tile

    if tile == 'yellow_key':
        unlock = unlock + 1
        maze[row][column] = 0 # 0 is 'empty' tile
    elif tile == 'yellow_door' and unlock > 0:
        unlock = unlock - 1
        maze[row][column] = 0 # 0 is 'empty' tile
    # enemy movement
    row = int(enemy.y / TILE_SIZE)
    column = int(enemy.x / TILE_SIZE)
    row = row + enemy.yv
    tile = tiles[maze[row][column]]
    if not tile == 'block':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy, duration=0.1, pos=(x, y))
    else:
        enemy.yv = enemy.yv * -1
    if enemy.colliderect(player):
        print("You died")
        exit()

    row = int(ghost.y / TILE_SIZE)
    column = int(ghost.x / TILE_SIZE)
    row = row + ghost.yv
    tile = tiles[maze[row][column]]
    if not tile == 'block':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(ghost, duration=0.1, pos=(x, y))
    else:
        ghost.yv = ghost.yv * -1
    if ghost.colliderect(player):
        print("You died")
        exit()

    row = int(enemy2.y / TILE_SIZE)
    column = int(enemy2.x / TILE_SIZE)
    row = row + enemy2.yv
    tile = tiles[maze[row][column]]
    if not tile == 'block':
        x = column * TILE_SIZE
        y = row * TILE_SIZE
        animate(enemy2, duration=0.1, pos=(x, y))
    else:
        enemy2.yv = enemy2.yv * -1
    if enemy2.colliderect(player):
        print("You died")
        exit()

    def on_mouse_down(pos):
        if player.collidepoint(pos):
            sounds.eep.play()
            player.image = 'pacman'