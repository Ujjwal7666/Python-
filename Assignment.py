#!/usr/bin/env python
# coding: utf-8

# Write a program that checks if a given number is even or odd and prints the result

# In[6]:


number=int(input("Enter a number"))
if ((number%2)==0):
    print(f"{number} is even ")
    
else :
    print(f" {number} is odd")


# Write a program that takes the temperature as input and classifies it into "Cold," "Moderate," or "Hot" based on the following conditions:
# Cold: Temperature <= 0
# Moderate: 0 < Temperature <= 25
# Hot: Temperature > 25

# In[15]:


temperature=float(input("Enter the temperature"))
if (temperature<=0):
    print(f"{temperature} is a Cold Temperature")
elif (0<temperature<=25):
    print(f"{temperature} is a Moderate Temperature")
else:
    print(f"{temperature} is a Hot Temperature")


# Write a program that checks if a given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.

# In[ ]:





# In[55]:


year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year!")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")


# Write a program that takes a person's age as input and determines their movie ticket price based on the following conditions:
# Below 5 years: Free
# 5 to 12 years: Rs.1000
# 13 to 18 years: Rs.1500
# 19 to 60 years: Rs.2000
# Above 60 years: Rs.2500
# 

# In[82]:


year=int(input("Enter your age:"))

if year<5:
    print("The movie ticket is free")
elif 5 <= year <=12:
    print("The movie ticket price is 1000!")
elif 13<=year<=18:
    print("The movie ticket price is 1500!")
elif 19<=year<=60:
    print("The movie ticket price is 2000!")
else :
    print("The movie ticket price is 2500!")


# :Create a Python script that prints the first 10 numbers in the
#     Fibonacci sequence..

# In[1]:


a=1
b=1
for i in range(1,6):
    print(a)
    print(b)
    a=a+b
    b=b+a


# In[2]:


#Implement a function to check if a given number is prime


# In[6]:


c=0
num=int(input("Enter a number"))
for i in range(1, num+1):
    if num%i==0:
        c=c+1
    if c==2:
        print("prime")
    else:
        print("composite")
        break
        


# In[8]:


#check palindorme
def is_palindrome(word):
    
    cleaned_word = ''.join(word.lower().split())

    return cleaned_word == cleaned_word[::-1]

# Example usage:
word_to_check = str(input("Enter a word to check"))
result = is_palindrome(word_to_check)

if result:
    print(f"{word_to_check} is a palindrome.")
else:
    print(f"{word_to_check} is not a palindrome.")
      


# In[13]:


#Implement a function that calculates the area of a regtangle given its length and breadth.
def regtangle_area(length, breadth):
    area=length*breadth
    return area
length_of_rectangle=float(input("Enter a lenght of rectangle: "))
breadth_of_rectangle=float(input("Enter a breadth of rectangle: "))

area_of_rectangle= regtangle_area(length, breadth)
print(f"The area of the rectangle with length {length_of_rectangle} and breadth {breadth_of_rectangle} is: {area_of_rectangle}")


# In[ ]:




