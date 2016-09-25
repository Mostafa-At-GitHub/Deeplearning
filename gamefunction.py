import numpy as np
def loc_of_enemy(arr):
    des = arr.shape[0]
    print des
    for x in xrange(0, arr.shape[0]):
        if arr[x,0] == 0 and arr[x, 1] == 1:
            print arr[x, :]
            return (arr[x,2], arr[x,3])
    return (0, 0)
a = np.empty([2, 4], dtype=int)
loc_of_enemy(a)