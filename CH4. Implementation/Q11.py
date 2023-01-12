# Q11. 뱀


import time
import os




def printField(field):
    os.system("cls")
    
    for i in field:
        print(i)
        
    print("")
        
    time.sleep(3)


field_size = int(input())

apples = []
for _ in range(0, int(input())):
    apples.append(list(map(int, input().split())))
    
commands = []
for _ in range(0, int(input())):
    commands.append(list(input().split()))





field = [[0] * field_size for _ in range(0, field_size)]

field[0][0] = 7

x,y = 0, 0

direction = 0

# for apple in apples:
#     field[apple[0] - 1][apple[1] - 1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]



printField(field)

for command in commands:   
    for _ in range(0, int(command[0])):
        x = x + dx[direction % 4]
        y = y + dy[direction % 4]
        
        field[y][x] = 7
        
        printField(field)
        
    if command[1] == "D":
        direction = direction + 1
    if command[1] == "L":
        direction = direction - 1
    





printField(field)