from util import *
# cups = ints(list('389125467'))
cups = ints(list('716892543'))

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
    if firstnode == None:
        firstnode = newnode
    if prev:
        prev.n = newnode
    prev = newnode
for i in range(10, 1000 * 1000 + 1):
    newnode = ListNode(i, prev, None)
    nodes[i] = newnode
    prev.n = newnode
    prev = newnode

lastnode = newnode
lastnode.n = firstnode
firstnode.p = lastnode

limit = lastnode.value

curr = firstnode
for _ in range(10 * 1000 * 1000):
    one   = curr.n
    two   = curr.n.n
    three = curr.n.n.n
    four  = curr.n.n.n.n

    curr.n = four
    four.p = curr

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

print(curr.n.value * curr.n.n.value)
