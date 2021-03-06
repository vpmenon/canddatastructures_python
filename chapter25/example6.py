# Chapter 25.5
# GARBAGE COLLECTION- THE FIRST METHOD


TRUE = 1
FALSE = 0

class snode:
    def __init__(self):
        self.op = 0
        self.next = None

def sEmpty(s):
    if(s == None):
        return TRUE
    else:
        return FALSE

def sPush(s, op):
    #pushes op in stack s.
    ptr = snode()
    ptr.op = op
    ptr.next = s
    s = ptr
    return s

def sTop(s):
    # returns top op from stack s without popping
    if(sEmpty(s) == None):
        return None
    return s.op

def sPop(s):
    # pops op from top of stack s.
    ptr = s
    if(sEmpty(s) == TRUE):
        return None
    s = s.next
    op = ptr.op
    return op

class node:

    def __init__(self):
        self.mark = 0
        self.val = 0
        self.horiz =None
        self.vert = None

def newNode():
    return node()

def createList():
    # return a dummy list created
    ptr = None
    s = None
    nineptr = node()
    ptr =newNode()
    s = sPush(s, ptr)
    ptr.val = 1
    ptr.horiz = node()
    ptr = ptr.horiz
    s = sPush(s, ptr)
    ptr.val = 2
    ptr.vert = node()
    s = sPush(s, ptr)
    ptr.val = 3
    ptr.vert = node()
    ptr = ptr.vert
    ptr.val = 4
    ptr = sPop(s)
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.val = 5
    ptr.horiz = newNode()
    ptr = ptr.horiz
    s = sPush(s, ptr)
    sixptr = ptr
    ptr.val = 6
    ptr.vert = newNode()
    ptr =ptr.vert
    ptr.val = 7
    ptr= sPop(s)
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.val = 8
    ptr = sPop(s)
    ptr.horiz = newNode()
    s = sPush(s, ptr)
    nineptr = ptr
    ptr.val = 9
    ptr.vert = newNode()
    ptr = ptr.vert
    ptr.val = 10
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.val = 11
    ptr = sPop(s)
    ptr.horiz = newNode()
    ptr = ptr.horiz
    ptr.vert = nineptr  # an internal link
    ptr.val = 12
    ptr.horiz = newNode()
    ptr = ptr.horiz
    s = sPush(s, ptr);
    ptr.val = 13
    ptr.vert = newNode()
    ptr = ptr.vert
    ptr.val = 14
    ptr.horiz = sixptr  # an internal link
    ptr = sPop(s)
    return sPop(s)

def markList(ptr):
    # print the horiz and vert lists iteratively using a stack
    s = None
    if(ptr != None or ptr.mark):
        return 0
    ptr.mark = TRUE
    print("marked = " + str(ptr.val) )
    s = sPush(s, ptr)
    while(sEmpty(s) != TRUE):
        while(TRUE):
            ptr = sPop(s)
            horiz = ptr.horiz
            if(horiz and horiz.mark == FALSE):
                horiz.mark = TRUE
                print("marked = " + str(horiz.val))
                sPush(s, horiz)
            ptr = ptr.vert
            if(ptr == None or ptr.mark == TRUE):
                return ptr
            ptr.mark = TRUE
            print("marked= " + str(ptr.val))

def markListRec(ptr):
    # mark the list pointed to by ptr recursively
    while(ptr != None and ptr.mark == FALSE):
        ptr.mark = TRUE
        print("marked= " + str(ptr.val))
        markListRec(ptr.vert)
        ptr = ptr.horiz

def main():
    head = createList()
    markListRec(head)
    markList(head)

main()





