from collections import deque
import time

# visiting neighboring nodes
# (x - 1, y) = up
# (x + 1, y) = down
# (x, y + 1) = right
# (x, y - 1) = left
# (x - 1, y - 1) =  315 degrees
# (x + 1, y + 1) =  135 degrees
# (x + 1, y - 1) =  225 degrees
# (x - 1, y + 1) =  45  degrees

# m x n size of the grid
GridRow = 7
GridCol = 7

# Goal State
Endlist = {(1, 1)}

# obstacles on the grid
blacklist = {}
# blacklist = {(3,2),(3,3),(3,4),(3,5),(3,6),(4,1),(5,2),(5,6)}
# blacklist = {(2,1), (2,2), (2,3), (2,4), (2,5), (3,5), (4,5), (4,4), (4,3), (4,2),(3,0),(4,6)}

visitedlist = deque()

start = time.time()
def BreadthFirstSearch(startx, starty):
    queue = deque([(startx, starty)])   # queue initialise with start node
    distance = {(startx, starty): 0}    # distance between node and current node

    while queue:
        x, y = queue.popleft()
        vcoord = (x, y)
        print(vcoord)

        for new_x, new_y in [(x - 1, y),(x, y - 1), (x, y + 1), (x + 1, y)]:
        #for new_x, new_y in [(x - 1, y),(x, y - 1),(x, y + 1),(x + 1, y),(x -1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)]:
            if 0 <= new_x < GridRow and 0 <= new_y < GridCol:
                coord = new_x, new_y
                visitedlist.append((vcoord,coord))

                if coord in blacklist:
                    continue
                elif coord in Endlist:
                    distance[coord] = distance[x, y] + 1
                    queue.append(coord)
                    print(queue)
                    print("Path Found. Distance is: " + str(distance[coord]))
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    return print(distance)
                elif coord not in distance:
                    distance[coord] = distance[x, y] + 1
                    queue.append(coord)
                    print(queue)
    if Endlist not in queue:
        print("Path not found")
        end = time.time()
        print('Evaluation time: {}s'.format(round(end - start, 7)))
    return print(distance)




BreadthFirstSearch(3, 2)
