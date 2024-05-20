#ps1
# a = input()
# print(a[1::2]+a[::2]) 
#ps2
# s = input()
# a = input()
# c = 0
# for i in s:
#     if i==a:
#         c += 1
# print(c)
#ps3
# s = input()
# a = input()
# c = 0
# for i in range(0,len(s),2):
#     if s[i]==a:
#         c += 1
# print(c)
#ps4
# s = input()
# for i in s:
#     if i not in "aeiouAEIOU":
#         print("NO")
#         break
# else:
#     print("YES")
#ps5
# s = input()
# if s.isdecimal():
#     print("YES")
# else:
#     print("NO")
#ps6
# import string
# s = input()
# v = c = 0
# for i in s:
#     if i in "aeiouAEIOU":
#         v+=1
#     elif i  in string.ascii_letters:
#         c+=1
# print(v,c)
#ps7
# s = input()
# s1 = ""
# c = 1
# for i in range(1,len(s)):
#     if s[i] == s[i-1]:
#         c+=1
#     else:
#         s1 += s[i-1]+str(c)
#         c = 1 
# s1 += s[i]+str(c)
# print(s1)
# s = input()
# s1 = ""
# i = 1
# while i<len(s):
#     c = 1
#     r = s[i]
#     while i<len(s) and  s[i] == s[i-1]:
#         c+=1
#         i+=1
#     else:
#         i+=1
#         s1 += r+str(c)
#         c = 1
# print(s1)

#ps8
# for _ in range(int(input())):
#     s = input().split()
#     v = 0
#     c = 0
#     for j in s:
#         for i in j:
#             if i in "aeiouAEIOU":
#                 v += 1
#             elif i.isalpha():
#                 c += 1
#     print(len(s),v,c)

# ps9
# for _ in range(int(input())):
#     a,b = input().split()
#     s = ""
#     for i in b:
#         if i not in a:
#             s += i
#     print(s)

#ps10
# for _ in range(int(input())):
#     a,b = input().split()
#     b = int(b)
#     s = ""
#     for i in a:
#         k = ord(i) + b
#         if k<=122:
#             s+=chr(k)
#         else:
#             s+=chr(96+k-122)
#     print(s)

#ps11
# class classa:
#     def factorial(self,n):
#         f = 1
#         for i in range(2,n+1):
#             f *= i
#         print(f)
# ob = classa()
# ob.factorial(5)

class classa:
    def __init__(self,n):
        self.n = n
    
    def factorial(self):
        def fact(n):
            if n==1:
                return 1
            return n*fact(n-1)
        print(fact(self.n))

ob = classa(5)
ob.factorial()