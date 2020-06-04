# Write your code here :-)
TILE_SIZE = 50
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 10

tiles = ['path', 'block', 'reward', 'yellow_key', 'yellow_door']
unlock = 0

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 3, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 4, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Actor("pacman", anchor=(0, 0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
enemy = Actor("ghost", anchor=(0, 0), pos=(5 * TILE_SIZE, 8 * TILE_SIZE))

enemy.yv = -1

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
    elif tile == 'yellow_key':
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

    def on_mouse_down(pos):
        if player.collidepoint(pos):
            sounds.eep.play()
            player.image = 'pacman'