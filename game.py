import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height, my_id = [int(i) for i in raw_input().split()]
def danger(x, y):

# game loop
while True:
    dangeon = np.empty([11, 13], dtype=int)
    for i in xrange(height):
        row = raw_input()
        dangeon[i, :] = row
        print >> sys.stderr, row
    entities = int(raw_input())
    pieces = np.empty([entities, 6], dtype=int)
    for i in xrange(entities):
        entity_type, owner, x, y, param_1, param_2 = [int(j) for j in raw_input().split()]
        pieces[i, :] = (entity_type, owner, x, y, param_1, param_2)
        print >> sys.stderr, "entity_type ", entity_type
        print >> sys.stderr, "owner ", owner
        print >> sys.stderr, "x ", x
        print >> sys.stderr, "y ", y
        print >> sys.stderr, "param_1 ", param_1
        print >> sys.stderr, "param_2 ", param_2

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print "BOMB 6 5"
