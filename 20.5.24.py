#p1-valid anagram
"""from collections import Counter
s=input()
s1=input()
d=Counter(s)
e=Counter(s1)
if d==e:
    print("s")
else:
    print("n")"""
#p2-implentation of stack using classes
"""class stack:
    def __init__(self):
        self.l=[]
        self.size=64
    def push(self,x):
        if len(self.l)!=self.size:
            self.l.append(x)
            print(self.l)
        else:
            print("full")
    def pop(self):
        self.l.pop()
        print(self.l)
    def peek(self):
        return self.l[-1]
o=stack()
o.push(3)
o.push(35)
o.push(3)
o.pop()
print(o.peek())"""
#p3-expression evulation
"""s=input()
st=[]
for i in s:
    if i.isdigit():
        st.append(int(i))
    else:
        a=st.pop()
        b=st.pop()
        if(i =="+"):
            st.append(a+b)
        elif(i =="-"):
            st.append(a-b)
        elif(i =="*"):
            st.append(a*b)
        else:
            st.append(a/b)
print(st[-1])
print(st)"""
#p4-implementing queues and stacks
"""s=[1,2,3,4,5,6,7,8,9,10,11,22]
n=3
f=0
while len(s)>1:
    if f==0:
        for i in range(n):
           if len(s)>1:
               a=s.pop(0)
        f=1
    else:
        for i in range(n):
            a=s.pop()
        f=0
print(a)
"""
#p5-isomorphicstring leetcode()
'''
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        if len(set(s))!=len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            else:
                if t[i]!=d[s[i]]:
                    return False
        return True
'''
#p6-valid parnathises
"""
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="{" or i=="[" or i=="(":
                st.append(i)
            else:
                if len(st)>0:
                    if i==")" and st.pop()!="(":
                        return False
                    elif i=="}" and st.pop()!="{":
                        return False
                    elif i=="]" and st.pop()!="[":
                        return False
                else:
                    st.append(i)
        return True if(len(st)==0) else False
"""
#p7- determine the color of chess board
"""class Solution:
    def squareIsWhite(self, c: str) -> bool:
        if (ord(c[0])+ int(c[1]))%2==0:
            return False
        return True
"""
"""
"""

