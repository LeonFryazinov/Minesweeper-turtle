def pos_in_array(pos,array):
    for i in array:
        if match_pos(i,pos):
            return True
    return False


def tuple_match(a,b):
    return a[0] == b[0] and a[1] == b[1]
def sum_tuple(a,b):
    return (a[0] + b[0],a[1] + b[1])

def sub_tuple(a,b):
    return (a[0] - b[0],a[1] - b[1])
def object_pos_taken(pos,objects):
    for object in objects:
        if object.match_pos(pos):
            return True
    return False
def match_pos(posA,posB):
    return posA[0] == posB[0] and posA[1] == posB[1]
def pos_in_bound(pos,max):
    xbound = pos[0] >= 0 and pos[0] <= max-1
    ybound = pos[1] >= 0 and pos[1] <= max-1
    return xbound and ybound