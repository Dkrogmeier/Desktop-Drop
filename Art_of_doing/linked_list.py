#linked_list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def insertBeginning(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    def insertEnd(self, newdata):
        newNode = Node(newdata)  #create node
        if self.head is None:    #if the list given does not have a value for head, then done
            self.head = newNode
            return
        last = self.head   #set a pointer to the head value
        while(last.next):   #while there are values in the list, update pointer
            last = last.next
        last.next = newNode  #connect last value to the new value

    def inbetween(self, middle, newdata):   #middle is the existing node that comes after our new one
        newNode = Node(newdata)
        if middle is None:
            print("The mentioned node is absent")
            return
        
        newNode = Node(newdata)
        newNode.next = middle.next  
        middle.next = newNode

    def remove(self, removeKey):
        headVal = self.head

        if (headVal is not None):
            if (headVal.data == removeKey):
                self.head = headVal.next
                headVal = None
                return

        while (headVal is not None):
            if headVal.data == removeKey:
                break
            prev = headVal
            headVal = headVal.next

        if (headVal == None):
            return

        prev.next = headVal.next

        headVal = None






#create new list
list = linked_list()
#set head of list to Mon
list.head = Node("Mon")
#create new nodes with data
e2 = Node("Tue")
e3 = Node("Wed")

#connect head node to next node
list.head.next = e2
e2.next = e3

#insert at beginning
list.insertBeginning("Sun")
list.insertEnd("Thurs")
list.inbetween(list.head.next, "Fri")
list.remove("Fri")
list.listprint()


look = [1, 2, 'seven']
