def addvec(a, b):
    return [x+y for x,y in zip(a,b)]

# TODO how do i DRY this out?

class dirscardinal:
    lst = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    tovec = {
        'E': [0, 1],
        'N': [1, 0],
        'W': [0, -1],
        'S': [-1, 0],
    }
    toname = {
        [0, 1]:  'E',
        [1, 0]:  'N',
        [0, -1]: 'W',
        [-1, 0]: 'S',
    }
    @staticmethod
    rot(direction, rotation):
        if rotation == 'R':
            return self.lst[(self.lst.index(d) - 1) % 4]
        elif rotation == 'L':
            return self.lst[(self.lst.index(d) + 1) % 4]
        else:
            raise Exception("invalid rotation direction: " + rotation)
    addvec = addvec

class dirsnatural:
    lst = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    tovec = {
        'R': [0, 1],
        'U': [1, 0],
        'L': [0, -1],
        'D': [-1, 0],
    }
    toname = {
        [0, 1]:  'R',
        [1, 0]:  'U',
        [0, -1]: 'L',
        [-1, 0]: 'D',
    }
    @staticmethod
    rot(direction, rotation):
        if rotation == 'R':
            return self.lst[(self.lst.index(d) - 1) % 4]
        elif rotation == 'L':
            return self.lst[(self.lst.index(d) + 1) % 4]
        else:
            raise Exception("invalid rotation direction: " + rotation)
    addvec = addvec

class dirsdigital:
    lst = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    tovec = {
        'R': [0, 1],
        'D': [1, 0],
        'L': [0, -1],
        'U': [-1, 0],
    }
    toname = {
        [0, 1]:  'R',
        [1, 0]:  'D',
        [0, -1]: 'L',
        [-1, 0]: 'U',
    }
    @staticmethod
    rot(direction, rotation):
        if rotation == 'R':
            return self.lst[(self.lst.index(d) + 1) % 4]
        elif rotation == 'L':
            return self.lst[(self.lst.index(d) - 1) % 4]
        else:
            raise Exception("invalid rotation direction: " + rotation)
    addvec = addvec
