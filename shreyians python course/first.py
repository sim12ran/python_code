## This program demonstrates the use of the ord() function to get the ASCII value of a character.
# a="A";
# print(ord(a))

## This program demonstrate the use of input and output function
# name=input("Enter your name:")
# print(f"Hello {name} Welcome to the showroom {name}");
# print(type(name))

##this program demonstrate the operation on variable and values
# a=int(input("enter first no."))
# b=int(input("enter second no."))
# c=a+b
# print("sum value is",c)

# print(a/b)
# print(a//b)

## logical operators working
# print(ord(input("Enter characters:")))

# print(ord("A"))
# print(ord("B"))
# print("ABC" > "ABD")
# print(int("A") > 34)   ##not possible to compare string and integer directly, it will raise a TypeError.

##print table of number
# a=input("enter your number:")
# for i in range(1,11):
#     print(f"{a} * {i} = {int(a)*i}")

##print factor of a number
# num=int(input("enter your number:"))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)

##to find perfect number
# num=int(input("enter your number:"))
# sum=0
# for i in range(1,num//2+1):
#     if(num%i==0):
#         sum=sum+i

# print(f"sum of the factor is {sum}")
# if(sum==num):
#     print("perfect number")
# else:
#     print("not perfect number")

##print the number is prime or not
# num=int(input("enter your number:"))
# count=0
# for i in range(2,num+1):
#     if(num%i==0):
#         count=count+1

# print(count)
# if(count>1):
#     print("not prime number")
# else:
#     print("prime number")

##To reverse a string
# str=input("enter your string:")
# for i in range(len(str)-1,-1,-1):
#     print(str[i],end=" ")

##to check digit, alpa, pecial character in string
# str=input("enter your string:")
# digit=0
# alpha=0
# special=0
# for i in str:
#     if(i.isdigit()):
#         digit+=1
#     elif(i.isalpha()):
#         alpha+=1
#     else:
#         special+=1

# print(f"digit is {digit}\n alphabet is {alpha}\n special character is {special}")

# print(dir(str))

##print reverse of a number
# a=245
# copy=a
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10

# print(rev)
# print(a)
# print(copy)
    
##random number guessing----------------------
# import random
# num=random.randint(1,10)
# print(num)
# tries=0

# while True:
#     guess=int(input("enter your guessing number"))
  
#     if(guess==num):
#       tries+=1
#       print(f"you have guessed the right number by trying {tries} times")
#       break
#     else:
#        tries+=1
#        print("sorry u are wrong")

# import random
# print(random.__file__)

##implementation of function-----------------
# def greet(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")    
# greet("Simran", "Kumari")

# def sum(b=45,a):
#     return a+b
# print(sum(5,21))

# help(list)

##List implementation----------------------
# num=[1,2,3,4,5]
# for i in num:
#     print(i, end="")

# fruits= ["mango","kiwi","litchi","banana"]
# for i in range(0,len(fruits)):
#     print(fruits[i],end=" ")
# print(fruits[3])  
 
# num=[24,-56,67,34,-12,-14,35]
# print("all positive number in the list")
# for i in num:
#     if(i>0):
#        print(i,end=" ")
# print("\nall negative number in the list")
# for i in num:
#     if(i<0):
#        print(i,end=" ")    
   
# num=[12,34,45,56,13,34,39]
# mean=0
# for i in num:
#     mean=mean+i
# print(mean)    
# print(f"mean of the number in the list is {mean//len(num)}")    

# num=[1,5,9,6,3]
# first_great=num[0]
# sec_great=num[0]
# for i in range(1,len(num)):
#      if(first_great<num[i]):
#          sec_great=first_great
#          first_great=num[i]

#      elif(num[i]>sec_great and num[i]<first_great):
#             sec_great=num[i]

# print(f"first greater is {first_great} and second greater is {sec_great}")

# for i in range(0,len(num)): 
#     if(great==num[i]):
#         print(f" the position of greatest element is {i}")  

## Implementation of  list----------------------
# a=(1,2,3,4,5,"man")
# print(a)
# a[0]=13     #not possible to change the value of tuple because it is immutable
# print(a)

# a=(1,2,3,4,5,5,5,5,print(),"hello")
# for i in a:
#     print(i)

# a=(1,)
# print(type(a))   #it is not a tuple because it is not enclosed in parentheses, it is an integer

# set ={1,2,3,4}
# for i in range(len(set)):
#     print(set[i], end=" ")

# a=[1,2,3,4,5]
# b=a.copy()
# b[0]=100
# print(b)
# print(a) 
# a[1]=23
# print(a)
# print(b)

# set ={1:10,20:20,3:30,4:40}
# for i in range(len(set)):
#     print(list(set.keys())[i], end=" ")

# d1={1:10,20:20,3:30,4:40}       ----merge two dictionary
# d2={5:50,6:60,7:70,8:80}
# d1.update(d2)
# print(d1)

# d1={1:10,20:20,3:30,4:40}
# d2={5:50,6:60,7:70,8:80}
# d1=d2
# d1[1]=100
# # for i in d2:
# #     d1[i]=d2[i]
# print(d1) 
# print(d2)             

# lis=[1,1,1,1,2,2,2,3,3,3,4,4,4,5,6,7]
# d={}
# for i in lis:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
# type(d) 

## FIle Hnadling------------------
# p=open(r'C:\Users\simra\OneDrive\Desktop\python-4-Ai\hello.py')
# print(p.read())

p=open(r'C:\Users\simra\OneDrive\Desktop\python-4-Ai\shreyians python course\first.py')
print(p.read())
