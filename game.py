import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height, my_id = [int(i) for i in raw_input().split()]
def loc_of_enemy(arr):
    for x in xrange(0, arr.shape[0]):
        if arr[x,0] == 0 and arr[x, 1] == 1:
            return (arr[x,2], arr[x,3])
    return (0, 0)
def loc_of_self(arr):
    for x in xrange(0, arr.shape[0]):
        if arr[x,0] == 0 and arr[x, 1] == 0:
            return (arr[x,2], arr[x,3])
    return (0, 0)
def if_enemy_bomb(arr):
    for x in xrange(0, arr.shape[0]):
        if arr[x,0] == 1 and arr[x, 1] == 1:
            return (arr[x,2], arr[x,3])
    return (-1, -1)
def estimate_ene_des(prev, curr):
    diff = np.subtract(curr, prev)
    return np.add(curr, diff)
def if_box(sq):
    if sq == '0':
        return True
    else:
        return False
def box_heuristic(self, turn):
    if turn == 0:

# TODO write a numpy array indicate the possible number of the box to break
# TODO  detect if the destination is boomed place
# TODO if in 8 turn there is not to break the box, then move out to the closest box
#
# game loop
int turn = 0
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
    loc_ene_cur = loc_of_enemy(pieces)
    print >> sys.stderr, ex, ey
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    print "BOMB ", ex, " ", ey
    if turn % 8:

    turn++
