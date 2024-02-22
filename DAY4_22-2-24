#p1
'''s=str(input())
s=s.lower()
s=s.replace(" ","")
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
if(len(d)==26):
    print("pangram")
else:
    print("not")
'''
#p2
'''s=set("the quick brown fox jumps over the lazy dog")
a={'a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," "}
c=0
print(s)
for i in s:
      if i in a:
            c+=1
if(c>=26):
    print("pangram")
else:
    print("not ") '''
#p3
'''s=input()
#s==s.lower()
s1 = set(s)
if len(s1)== 27:
    print("pangram")
else:
    ("not")'''
#p4--using dictionaries
'''a={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s=input()
d={}
for i in s:
    if i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
x=d.keys()
print(d)
if(len(x)==26):
    print("yes")
else:
    print("NO")'''
#p5
'''s=input()
a={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
d={}
c=0
for i in s:
    if i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
print(d)

for i in d:
    if(d[i]>1):
        print(i)
        break'''
#p6--
'''x=int(input())
d={}
for i in range(x):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
print(d)  
x=max(d.values())
p=[]
for i in d:
    if d[i]==x:
        p.append(i)  
print(max(p),x)'''
#p7-- databses sum (gaby)
'''for i in range(int(input())):
    x,y=map(int,input().split())
    d={}
    for i in range(y):
        a,b =map(int,input().split())
        if b not in d:
            d[b]=[a]
        else:
            d[b].append(a)
    print(d)
    for j in d:
        if len(d[j])> a and len(set(d[j])!=len(d[j])):
            print(f"scenario#{j+1}:IMpoosible")
            break
    else:
            print(f"scenario#{j+1}:poosible")'''
#p8
'''
d={}
for i in range(int(input())):
    a,b=input().split()
    
    if a not in d:
        d[a]=[b]
    else:
        d[a].append(b)
print(d)
x=input("enter req:")

print(d.get(a,None))'''
#p9
x=int(input())
rev=0
while(x>0):
    rem=x%10
    rev=rev*10+rem
    x=x//10
print(rev)







