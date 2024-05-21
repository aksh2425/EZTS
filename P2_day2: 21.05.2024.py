class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.count=0
class Linkedlist:
    def __init__(self):
        self.head=None
        self.count=0
    def print_ll(self):
        if self.head is None:
            print("empty list")
        else:
            curr=self.head
            while(curr is not None):
                print(curr.data,end="->")
                curr=curr.next
            print("null")
    def add_beign(self,data):
        new_node=Node(data)

        if self.head==None:
            new_node=Node(data)
            self.head=new_node

        else:
            new_node.next=self.head
            self.head=new_node
        #print(self.head.data)
    def add_end(self,data):
        new_node=Node(data)
        if self.head== None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!= None:
                curr=curr.next
            curr.next=new_node
    def del_begin(self):
        if self.head ==None:
            print("its empty man")
            return 0
        else:
            self.head=self.head.next
    def del_end(self):
        if self.head==None:
            print("its emoty")
            return 0
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None
    def length(self):
        c=0
        curr=self.head
        while curr:
            c+=1
            curr=curr.next
           # c+=1
        return c
    def middle(self,data):
        new_node=Node(data)
        self.count = self.length()
        if self.count==1:
            self.head.next=new_node
        else:
            i=1
            half=self.count//2
            curr=self.head
            while i!=half:
                curr=curr.next
                i+=1
            new_node.next=curr.next
            curr.next=new_node
    def middle_pointer(self,data):
        new_node=Node(data)
        if self.head==None:
            print("empty")
        if self.count==1:
            self.head.next=new_node
        else:
        #new_node=Node(data)
            fast=self.head
            slow=self.head
            while(fast.next!=None and fast.next.next!=None):
                slow = slow.next
                fast =fast.next.next
            new_node.next=slow.next
            slow.next=new_node
    def del_middle(self): 
        fast=self.head
        slow=self.head
        temp=None
        while(fast.next!=None and fast.next.next!=None):
            temp=slow
            slow = slow.next
            fast =fast.next.next
        temp.next=slow.next
    def reverse(self):
        prev=None
        Next=None
        curr=self.head
        while(curr!=None):
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next
        self.head=prev
"""a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
print(a.data)
print(a.next)"""
ob=Linkedlist()
ob.add_beign(4)
ob.add_beign(3)
ob.add_beign(2)
ob.add_end(9)
ob.add_end(10)
ob.print_ll()
ob.reverse()
ob.print_ll()
