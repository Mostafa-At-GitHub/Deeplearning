import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height, my_id = [int(i) for i in raw_input().split()]

# game loop
while True:
    for i in xrange(height):
        row = raw_input()
        print row
    entities = int(raw_input())
    for i in xrange(entities):
        entity_type, owner, x, y, param_1, param_2 = [int(j) for j in raw_input().split()]
        print entity_type
        print owner
        print x
        print y
        print param_1
        print param_2

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print "BOMB 6 5"
