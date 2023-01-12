# Q11. 뱀
# [백준] www.acmicpc.net/problem/3190

import time
import os


field_size = int(input())

fields = [[0] * field_size for _ in range(0, field_size)]

apples = [list(map(int, input().split())) for _ in range(0, int(input()))]
apples = [[apple[0] - 1, apple[1] - 1] for apple in apples]

moves = [list(input().split()) for _ in range(0, int(input()))]
moves = [[int(move[0]), move[1]] for move in moves]

snakes = [[0, 0]]

for apple in apples:
    fields[apple[0]][apple[1]] = 1


def printField():
    os.system("cls")

    for i in range(0, field_size):
        for j in range(0, field_size):
            if [i, j] in snakes:
                print("X", end=" ")
            else:
                print(fields[i][j], end=" ")
        print("")

    time.sleep(0.5)


y = 0
x = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


direction = 0

count = 0

for move in moves:
    for _ in range(0, move[0]):
        printField()
        
        next_y = y + dy[direction]
        next_x = x + dx[direction]
        
        if next_x >= field_size or next_y >= field_size:
            print(count)
            exit(0)

        snakes.append([next_y, next_x])

        if [next_y, next_x] in apples:
            fields[next_y][next_x] = 0
        
        else:
            snakes.pop(0)
            
        count = count + 1

        y = next_y
        x = next_x
        

    if move[1] == "D":
        direction = (direction + 1) % 4
        count = count + 1

    if move[1] == "L":
        direction = (direction - 1) % 4
        count = count + 1
