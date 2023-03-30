import player1, player2
import random
import math

steps = 1
overall_rocks = random.randint(20, 65)
max_per_step = math.floor(math.sqrt(overall_rocks))

while overall_rocks != 0:
    if steps % 2 == 1:
        p1 = player1(overall_rocks, max_per_step)
        steps += 1
    else:
        p2 = player2(overall_rocks, max_per_step)
        steps += 1