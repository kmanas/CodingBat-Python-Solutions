#!/usr/bin/env python
# coding: utf-8

# ## String-1: Basic python string problems -- no loops.

# #### Problem 1
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

# In[47]:


def hello_name(name):
  return("Hello "+ name+"!")


# In[48]:


print(hello_name("Jupyter"))
print(hello_name("X"))
print(hello_name("Python"))


# #### Problem 2
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

# In[49]:


def make_abba(a, b):
  return a+b+b+a


# In[50]:


print(make_abba("Jupyter", "Notebook"))
print(make_abba("What", "Up"))
print(make_abba("Hi", "Bye"))


# #### Problem 3
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

# In[51]:


def make_tags(tag, word):
  return "<"+tag+">"+word+"<"+"/"+tag+">"


# In[52]:


print(make_tags('i','Hello'))
print(make_tags('title','String'))


# #### Problem 4
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

# In[53]:


def make_out_word(out, word):
  return out[:2] + word + out[2:]


# In[54]:


print(make_out_word("<<>>", "Yay"))
print(make_out_word("[[]]", "Woow"))
print(make_out_word("HiHi", "5"))


# #### Problem 5
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

# In[55]:


def extra_end(str):
  return str[-2:] * 3


# In[56]:


print(extra_end("Hihi"))
print(extra_end("Python"))
print(extra_end("Jupyter"))


# #### Problem 6
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". 

# In[57]:


def first_two(str):
  return str[:2]


# In[58]:


print(first_two("Hallo World"))
print(first_two("Hi"))
print(first_two("Notebook"))


# #### Problem 7
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

# In[59]:


def first_half(str):
    return str[:int(len(str)/2)]


# In[60]:


print(first_half("WooHoo"))


# #### Problem 8
# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

# In[61]:


def without_end(str):
  return str[1:-1]


# In[62]:


print(without_end("Coding"))
print(without_end("makes"))
print(without_end("strong"))


# #### Problem 9
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

# In[63]:


def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  else:
    return a+b+a


# In[64]:


print(combo_string("Hi", "Hello"))
print(combo_string("Stay", "Cool"))
print(combo_string("Love", "Python"))


# #### Problem 10
# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

# In[65]:


def non_start(a, b):
  return (a[1:] + b[1:])


# In[66]:


print(non_start("Hello", "There"))
print(non_start("hi", "yo"))
print(non_start("python", "code"))


# #### Problem 11
# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

# In[67]:


def left2(str):
  return str[2:] + str[:2]


# In[68]:


print(left2("python"))
print(left2("coding"))
print(left2("easy"))

