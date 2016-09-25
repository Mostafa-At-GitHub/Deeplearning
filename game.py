import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height, my_id = [int(i) for i in raw_input().split()]
def loc_of_enemy(arr):
    des = arr.shape[0]
    print des
    for x in xrange(0, arr.shape[0]):
        if arr[x,0] == 0 and arr[x, 1] == 1:
            print arr[x, :]
            return (arr[x,2], arr[x,3])
    return (0, 0)

# game loop
while True:
    dangeon = np.chararray((11, 13))
    for i in xrange(height):
        row = raw_input()
        dangeon[i, :] = row
        print >> sys.stderr, row
    entities = int(raw_input())
    pieces = np.empty([entities, 6], dtype=int)
    for i in xrange(entities):
        entity_type, owner, x, y, param_1, param_2 = [int(j) for j in raw_input().split()]
        pieces[i, :] = (entity_type, owner, x, y, param_1, param_2)
        # print >> sys.stderr, "entity_type ", entity_type
        # print >> sys.stderr, "owner ", owner
        # print >> sys.stderr, "x ", x
        # print >> sys.stderr, "y ", y
        # print >> sys.stderr, "param_1 ", param_1
        # print >> sys.stderr, "param_2 ", param_2
    ex, ey = loc_of_enemy(pieces)
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    print "BOMB ", ex, " ", ey
    print "BOMB 6 5"
