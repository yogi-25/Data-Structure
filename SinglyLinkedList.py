class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next

firstnode=node("yogita")
linkedlist=Linkedlist()
linkedlist.insert(firstnode)
secondnode=node("amruta")
linkedlist.insert(secondnode)
thirdnode=node("Dnyaneshawar")
linkedlist.insert(thirdnode)
linkedlist.printList()
