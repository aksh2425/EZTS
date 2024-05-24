# Leetcode - > 100,226,1022,112,637

class Graph:
    def __init__(self):
        self.d = {}

    def add(self,u,v):
        if u not in self.d:
            self.d[u] = [v]
        else:
            self.d[u].append(v)

    def bfs(self,root):
        q = [root]
        v = [root]
        while q:
            curr = q.pop(0)
            print(curr)
            for i in self.d[curr]:
                if i not in v:
                    v.append(i)
                    q.append(i)

g = Graph()
g.add(1,2)
g.add(3,1)
g.add(1,3)
g.add(2,1)
g.add(1,4)
g.add(4,1)
g.add(3,6)
g.add(6,3)
print(g.d)
g.bfs(1)