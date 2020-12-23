import itertools
import math
import collections

INPUT = '716892543'
CUP_COUNT = 1_000
MOVE_COUNT = 1_000
MAX_DIST = 1_000

class ListNode:
    def __init__(self, value, p, n):
        self.value = value
        self.p = p
        self.n = n
    def __str__(self):
        return f'ListNode(value={self.value}, p={self.p.value if self.p else None}, n={self.n.value if self.n else None})'
    def dist(self, other):
        left = self
        right = self
        for i in range(MAX_DIST):
            if other in [left, right]:
                return i
            left = left.p
            right = right.n
        return math.inf

nodes = {}

# Create a circular linked list of cups
prev = None
firstnode = None
for i in itertools.chain(
    (int(c) for c in INPUT),
    range(10, CUP_COUNT + 1),
):
    newnode = ListNode(i, prev, None)
    nodes[i] = newnode
    if firstnode is None:
        firstnode = newnode
    if prev:
        prev.n = newnode
    prev = newnode
newnode.n = firstnode
firstnode.p = newnode


curr = firstnode
distances = collections.Counter()
for _ in range(MOVE_COUNT):
    one   = curr.n
    two   = curr.n.n
    three = curr.n.n.n
    four  = curr.n.n.n.n

    # Pick up cups one, two, and three by removing them from the list
    curr.n = four
    four.p = curr

    # Find the destination cup
    destval = curr.value
    illegal = [curr.value, one.value, two.value, three.value]
    while destval in illegal:
        destval -= 1
        if destval == 0:
            destval = CUP_COUNT
    dest = nodes[destval]
    after = dest.n

    distances[curr.dist(dest)] += 1

    # Insert one-two-three between dest and after
    dest.n = one
    one.p = dest
    three.n = after
    after.p = three

    # Next cup
    curr = curr.n

# Find cup 1
while curr.value != 1:
    curr = curr.n

# Print the answer to part 2
# print(curr.n.value * curr.n.n.value)

# Print the distances
for d in sorted(distances):
    print(d, distances[d])
