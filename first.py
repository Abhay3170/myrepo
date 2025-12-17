# def railwayTicket(name,tino,age):
#     if(((name=='abhay' or name=='Abhay') and tino==1234) or ((name=='anmol' or name=='Anmol') and  tino==4321)):
#         price=80
#         if age>0 and age<=5:
#             price=80
#         elif age>5 and age<50:
#             price+=price*.12
#         elif age>=50 and age<=65:
#             price+=price*.06
#         else:
#             price-=price*.2
#         print("Kalka to Shimla")
#         print("Distance=80km")
#         print("Price of ticket=",price)
#     else:
#         print("Oops!! Passenger not found")
# n=input("Enter your name:")
# t=int(input("Enter your ticket number:"))
# a=int(input("Enter your age:"))
# railwayTicket(n,t,a)

# def fibbonaci(n):
#     a=0
#     b=1
#     if n<=0:
#         print("Invalid input")
#     elif n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# n=int(input("Enter the number of terms:"))  
# fibbonaci(n)

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(3))


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(3))

# def palindrome(n):
#     org=n
#     s=0
#     while n>0:
#         d=n%10
#         s=s*10+d
#         n//=10
#     if s==org:
#         print("PALINDROME numberr")
#     else:
#         print("Not")
# palindrome(151)

# def arm(n):
#     o=n
#     s=0
#     while n>0:
#         d=n%10
#         s=s+d**3
#         n//=10
#     if s==o:
#         print("True")
#     else:
#         print("False")
# arm(153)

# def prime(n):
#     num=int(n**0.5)
#     for i in range(2,num):
#         if n%i==0:
#             return False
#         return True
# if prime(11):
#     print("True")
# else:
#     print("False")

# def vowels(s):
#     v=0
#     for c in s:
#             if c in 'aeiou':
#                 v=v+1
#     return v
# print(vowels("Abhay"))

# def gcd(a,b):
#     while b!=0:
#         temp=b
#         b=a%b
#         a=temp
#     return a
# print(gcd(18,36))

# def fib(n):
#     a=0
#     b=1
#     if n==0:
#         return a
#     if n==1:
#         return a,b
#     if n>1:
#         print(a)
#         print(b)
#         for i in range(n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# print(fib(5))

# def word_freq(s):
#     for i  in s:
#         print(f"{i} in {s} = {s.count(i)}")
# s="abhay"
# word_freq(s)

list1=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(list1)
cols=len(list1[0])
transpose=[]

for i in range(cols):
    new=[]
    for j in range(rows):
        new.append(list1[j][i])
    transpose.append(new)
for rows in transpose:
    print(rows)

a=[[1,4],[2,5],[3,6]]
rows=len(a)
cols=len(a[0])
transpose=[]
for i in range(cols):
    new_row=[]
    for j in range(rows):
        new_row.append(a[j][i])
    transpose.append(new_row)
print("Transpose of matrix:")
for row in transpose:
    print(row)