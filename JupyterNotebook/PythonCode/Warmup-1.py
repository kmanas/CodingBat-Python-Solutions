#!/usr/bin/env python
# coding: utf-8

# ## Warmup-1: Simple warmup problems to get started, no loops

# #### Problem 1
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

# In[2]:


def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False


# In[3]:


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))


# #### Problem 2
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# In[4]:


def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile


# In[5]:


print(monkey_trouble(True, True))
print(monkey_trouble(True, False))
print(monkey_trouble(False, False))


# #### Problem 3
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

# In[6]:


def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b


# In[7]:


def sum_double(a, b):
  return (a+b)*2 if a == b else a+b


# In[8]:


print(sum_double(3,2))
print(sum_double(1,4))
print(sum_double(3,3))


# #### Problem 4
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

# In[9]:


def diff21(n):
  if n > 21:
    return (n-21)*2
  else:
    return 21-n


# In[10]:


print(diff21(10))
print(diff21(21))
print(diff21(4))


# #### Problem 5
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# In[11]:


def parrot_trouble(talking, hour):
  if talking and hour > 20:
    return True
  if talking and hour < 7:
    return True
  else:
    return False


# In[12]:


print(True, 21)
print(False, 21)
print(False, 12)


# #### Problem 6
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

# In[13]:


def makes10(a, b):
  return a == 10 or b == 10 or (a+b==10)


# In[14]:


print(makes10(9,9))
print(makes10(10,10))
print(makes10(12,-2))


# #### Problem 7
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

# In[15]:


def near_hundred(n):
  if (90 <= n <= 110) or (190 <= n <= 210):
    return True
  else:
    return False


# In[16]:


print(near_hundred(121))
print(near_hundred(-101))
print(near_hundred(93))


# #### Problem 8
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

# In[17]:


def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))


# In[18]:


print(pos_neg(1,-1, False))
print(pos_neg(1,2, True))
print(pos_neg(5,-5, False))


# #### Problem 9
# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. 

# In[19]:


def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return ("not " + str)


# In[20]:


print(not_string("candy"))
print(not_string("not"))
print(not_string("x"))
print(not_string("not bad"))


# #### Problem 10
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

# In[21]:


#Converting to list and using del:
def missing_char(str, n):
  arr = list(str)
  del (arr[n])
  newstr= "".join(arr)
  return newstr


# In[22]:


#Removing char by using replace():
def missing_char(str, n):
  char = str[n]
  newstr = str.replace(char, "")
  return newstr


# In[23]:


print(missing_char("hi", 0))
print(missing_char("codebat", 3))
print(missing_char("code", 1))


# #### Problem 11
# Given a string, return a new string where the first and last chars have been exchanged.

# In[24]:


def front_back(str):
  newstr = ""
  if len(str) > 1:
    newstr = str[-1] + str[1:-1] + str[0]
    return newstr
  else:
    return str


# In[25]:


print(front_back("Codebat"))
print(front_back("abc"))
print(front_back("Hallo"))


# #### Problem 12
# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

# In[26]:


def front3(str):
  return (str[:3] * 3 if len(str) >= 3 else str * 3 )


# In[27]:


print(front3("Python"))
print(front3("notebook"))
print(front3("Jupyter"))

