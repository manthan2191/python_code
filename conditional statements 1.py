#!/usr/bin/env python
# coding: utf-8

# ## write a program to print given number is even or odd

# In[2]:



num=int(input("enter a number"))
if num%2 == 0: 
    print("even")
else:
        print("odd")


# ## write a program to check given year is leap year or not

# In[1]:



num=int(input("enter a number"))
if num%4 == 0:
    print("leap year")
else:
    print("not leap year")


# ## write a program to find after selling there is profit or loss

# In[2]:



a=int(input("enter selling price of product"))
b=int(input("enter buying price of product"))
if a>b:
    print("we are in profit ")
else:
    print("we are in loss ") 


# ## write a program to enter three numbers and find gretest number 

# In[3]:



a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
largest = 0
if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c
print(largest, "is the largest of three numbers.")


# ## write a program to check whether a person is eligible to vote or not

# In[4]:


age = int(input("Enter age of a user: "))

if age >= 18:
    print("User is eligible for voting: ")
else:
    print("User is not eligible for voting: ")


# ## write a program to check given number is positive or negative

# In[5]:


num=int(input("enter a number"))
if num<0:
    print("given number is negative")
else:
    print("given number is positive")


# In[ ]:




