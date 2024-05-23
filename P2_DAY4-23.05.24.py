#trees
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
"""t=Node(1)
t1=Node(2)
t2=Node(3)
t.left=t1
t.right=t2
print(t.right.data)"""
class Trees:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=Node(data)
        if self.root==None:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if curr.data < data:
                    if curr.right==None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
                else:
                    if curr.left==None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
    def count_root(self,root):
        curr=root
        def count(root):
            if root==None:
                return 0
            else:
                leftnode=count(root.left)
                rightnode=count(root.right)
            return leftnode+rightnode+1
        a=count(curr)
        return a

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def searchnode(self,root,data):
        s=self.search(self.root,data)
        if s!=None:
            print("found")
        else:
            print("notfound")
    def search(self,root,data):
        if root==None or root.data==data:
            return root
        else:
            return self.search(root.left,data) or self.search(root.right,data)

t=Trees()
t.insert(5)
t.insert(3)
t.insert(4)
t.insert(7)
t.insert(6)
#t.inorder(t.root)
print(t.count_root(t.root))
t.searchnode(t.root,8)
