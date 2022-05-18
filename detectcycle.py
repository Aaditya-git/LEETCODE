class Node:
    def __init__(self,data):
        self.data = data
        Node.next = None

def cycle(head):
    slow = head
    fast = head
    flag = 0
    while(slow!=None and fast!=None and fast.next!=None):
        fast = fast.next.next
        slow = slow.next

        if(fast==slow):
            flag = 1
            break

    if(flag):
        slow = head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next

        return slow
    return None

head = Node('a')
nodeb = Node('b')
nodec = Node('c')
noded = Node('d')
nodee = Node('e')
nodef = Node('f')
nodeg = Node('g')
nodeh = Node('h')
nodei = Node('i')
nodej = Node('j')



head.next = nodeb
nodeb.next = nodec
nodec.next = noded
noded.next = nodee
nodee.next = nodef
nodef.next = nodeg
nodeg.next = nodeh
nodeh.next = nodei
nodei.next = nodej
nodej.next = noded



head = cycle(head)
print(head.data)
