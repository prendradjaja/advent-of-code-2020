from util import *
cups = ints(list('716892543'))
limit = len(cups)
# cups = ints(list('123'))

nodes = {}

class ListNode:
    def __init__(self, value, p, n):
        self.value = value
        self.p = p
        self.n = n
    def __str__(self):
        return f'ListNode({self.value}, {self.p.value if self.p else None}, {self.n.value if self.n else None})'

prev = None
firstnode = None
for c in cups:
    newnode = ListNode(c, prev, None)
    nodes[c] = newnode
    if not firstnode:
        firstnode = newnode
    if prev:
        prev.n = newnode
    prev = newnode
lastnode = newnode
lastnode.n = firstnode
firstnode.p = lastnode

curr = firstnode
for _ in range(100):
    one   = curr.n
    two   = curr.n.n
    three = curr.n.n.n
    four  = curr.n.n.n.n

    curr.n = four
    four.p = curr

    # one.p = None
    # three.n = None

    destval = curr.value
    illegal = [curr.value, one.value, two.value, three.value]
    while destval in illegal:
        destval -= 1
        if destval == 0:
            destval = limit

    dest = nodes[destval]
    afterdest = dest.n

    dest.n = one
    one.p = dest
    three.n = afterdest
    afterdest.p = three

    curr = curr.n

while curr.value != 1:
    curr = curr.n

curr = curr.n

while curr.value != 1:
    print(curr.value, end='')
    curr = curr.n
print()
