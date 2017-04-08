
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd


# In[3]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[4]:

s


# In[5]:

s.index


# In[6]:

pd.Series(np.random.randn(5))


# In[7]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[8]:

d


# In[9]:

pd.Series(d)


# In[10]:

pd.Series(d, index=['b', 'c', 'd', 'a']) # NaN (not a number) is the standard missing data marker used in pandas


# In[11]:

s


# In[12]:

s[0]


# In[13]:

s[:3]


# In[14]:

s[s > s.median()]


# In[15]:

s.max()


# In[16]:

s.min()


# In[17]:

s[[4, 3, 1]]


# In[18]:

np.exp(s)#exponent


# In[19]:

s['a']


# In[20]:

s['e'] = 12.


# In[21]:

s


# In[22]:

'f' in s


# In[23]:

if 'e' in s:
    print(s['e'])


# In[24]:

'a' in s


# In[25]:

s.get('f')


# In[26]:

s.get('a')


# In[27]:

s.get('f', np.nan)


# In[28]:

s + s


# In[29]:

s * 3


# In[30]:

s * 2


# In[31]:

s / 0.5


# In[32]:

s


# In[33]:

s[1:] + s[:-1]


# In[34]:

s[1:]


# In[35]:

s[:-1]


# In[36]:

s = pd.Series(np.random.randn(5), name='something')


# In[37]:

s


# In[38]:

s['f'] = 0


# In[39]:

s


# In[40]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[41]:

d


# In[42]:

df = pd.DataFrame(d)#create a table


# In[43]:

df


# In[44]:

pd.DataFrame(d, index=['d', 'b',])


# In[46]:

pd.DataFrame(d, index=['d', 'b',])


# In[49]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three', 'one'])


# In[50]:

df.index


# In[51]:

df.columns


# In[52]:

d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}


# In[53]:

pd.DataFrame(d)


# In[54]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[55]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[56]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[57]:

data


# In[58]:

pd.dataframe[:] = [(1,2.,'Hello'), (2,3.,"World")]#wrong


# In[59]:

pd.DataFrame(data)


# In[60]:

pd.DataFrame(data, index=['first', 'second'])


# In[61]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[62]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[63]:

pd.DataFrame(data2)


# In[64]:

pd.DataFrame(data2, index=['first', 'second'])


# In[65]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[66]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
 


# In[67]:

data


# In[68]:

data2


# In[69]:

df


# In[70]:

df['one']


# In[71]:

df['three'] = df['one'] * df['two']


# In[72]:

df['three']


# In[73]:

df


# In[74]:

df['flag'] = df['one'] > 2


# In[75]:

df


# In[76]:

del df['two']#del is remove


# In[77]:

df


# In[78]:

three = df.pop('three')# remove colmn three


# In[79]:

df


# In[80]:

df['foo'] = 'bar'


# In[81]:

df


# In[82]:

three


# In[83]:

df['three']


# In[84]:

df['three']= 1.5


# In[85]:

df


# In[86]:

df['one_trunc'] = df['one'][:2]


# In[87]:

df


# In[88]:

three = df.pop('three')


# In[89]:

df


# In[90]:

df['one_trunc'] = df['one'][:2]


# In[91]:

df


# In[ ]:



