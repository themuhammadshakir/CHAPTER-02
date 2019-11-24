#!/usr/bin/env python
# coding: utf-8

# # MUHAMMAD SHAKIR(19B-096-SE)

# # CHAPTER 02:EXERCISE

# # 2.11(a)

# In[1]:


n = -7
sums=0
while (n <= -1):
    sums += n
    n = n + 1
print ("SUM OF NEGATIVE INTEGER THROUGH -7 TO -1 IS : ", sums)


# # 2.11(b)

# In[8]:


# GROUP 1
a = 17
b = 9
print("AVERAGE AGE OF GROUP 1 IS : ",(a+b)/2)
# GROUP 2
c = 24
d = 10
print("AVERAGE AGE OF GROUP 2 IS : ",(c+d)/2)
# GROUP 3
e = 21
f = 11
print("AVERAGE AGE OF GROUP 3 IS : ",(e+f)/2)
# GROUP 4
g = 27
h = 12
print("AVERAGE AGE OF GROUP 4 IS : ",(g+h)/2)
print("AVERAGE AGE OF GROUPS KIDS IS : ",(((a+b)/2) + ((c+d)/2) + ((e+f)/2) + ((g+h)/2))/4)


# # 2.11(c)

# In[15]:


x = 2 ** -20
print(x)


# # 2.11(e)

# In[20]:


x = (4365)
print(x%61)


# # 2.14(a)

# In[47]:


s = 'goodbye'
print(len(s))
s[0] == 'g'


# # 2.14(b)

# In[48]:


s = 'goodbye'
print(len(s))
s[6] == 'g'


# # 2.14(c)

# In[51]:


s = 'goodbye'
print(len(s))
s[0:1] == 'ga'


# # 2.14(d)

# In[55]:


s = 'goodbye'
print(len(s))
s[6] == 'x'


# # 2.14(e)

# In[60]:


s = 'goodbye'
print(len(s))
s[3] == 'd'


# # 2.14(f)

# In[62]:


s = 'goodbye'
print(len(s))
s[0]==s[6]


# # 2.14(g)

# In[65]:


s = 'goodbye'
print(len(s))
s[4]+s[5]+s[6] == 'tion'


# # 2.15(a)

# In[69]:


a = 'anachronistically'
b = 'counterintuitive'
c = len(a)
d = len(b)
c == d + 1


# # 2.15(c)

# In[76]:


a = 'floccinaucinihilipilification'
'e' in a


# # 2.15(d)

# In[90]:


a = 'counterrevolution'
b = 'counter'
c = 'resolution'
len(b) + len(c) == len(a)


# # 2.18(a)

# In[2]:


flowers = ['rose','bougainvillea','yucca','marigold','daylilly','lilly of the vally']


# # 2.18(b)

# In[3]:


flowers = ['rose','bougainvillea','yucca','marigold','daylilly','lilly of the vally']
'potato' in flowers


# # 2.18(c)

# In[ ]:


thorny = ['rose','bougainvillea','yucca']


# # 2.18(d)

# In[4]:


poisonous = ['lilly of the vally']


# # 2.18(e)

# In[5]:


thorny = ['rose','bougainvillea','yucca']
poisonous = ['lilly of the vally']
dangerous = thorny + poisonous
print(dangerous)


# # 2.27

# In[27]:


from math import sin 
length = eval(input("ENTER LENGTH : "))
angle = eval(input("ENTER ANGLE IN DEGREE : "))
rad = (3.142*angle)/180
height = length *sin(rad)
print(height,"m")


# In[ ]:





# In[ ]:





# In[ ]:




