#!/usr/bin/env python
# coding: utf-8

# # Assignment no. 2__ PIAIC91502

# In[3]:


import numpy as np


# In[39]:


# Task no 1

    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods 

def function1():
    x = np.arange(1,13).reshape((6,2))
    return x
function1()


# In[37]:


# Task no 2

 #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape
def function2():
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))
    return x

function2()


# In[12]:


# Task no 3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[] #wrtie your code here
    return x
    """


# In[16]:


def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[]
    #wrtie your code here
    return x
    


# In[28]:


a = np.arange(1, 100*10+1).reshape((100,10))
a

condition = np.mod(a,5)==0
np.extract(condition, a)


# In[29]:


# Task no 4

def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    print("orignal Array...")
    print(arr)
    print("after Swap columns 1 and 2 ")
    arr[:,[0, 1]] = arr[:,[1, 0]]
    print(arr)
    
function4()


# In[12]:


#Task no. 5

#Create a null vector of size 20 with 4 rows and 5 columns with numpy function

def function5():
    z = np.zeros((4,5))
    return z
function5()


# In[23]:


#Task no 6

# Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively

def function6():
    arr = np.zeros(10)
    arr[4] = 10
    arr[7] = 20
    return arr
function6()



# In[29]:


#Task no 7

#  Create an array of zeros with the same shape and type as X. Dont use reshape methoddef function():

def function7():
    x = np.arange(4, dtype = np.int64)
    arr = np.zeros_like(x)
    return arr
function7()


# In[32]:


# Task no 8

# Create a new array of 2x5 uints, filled with 6.

def function8():
    x = np.full((2,5), 6, dtype = np.uint)
    return x
function8()


# In[36]:


# Task no 9

# Create an array of 2, 4, 6, 8, ..., 100.

def function9():
    a = np.arange(2,101)
    return a
function9()


# In[ ]:


#task10
def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = # write your code here 
  
    return subt
     """
     Expected Output:
               array([[2 2 2]
                      [2 2 2]
                      [2 2 2]])


# In[5]:


def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = np.subtract(arr[0:,0:],brr[0,0:])
  
    return subt
function10()


# In[6]:


arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
 brr = np.array([1,2,3])
 subt = np.subtract(arr[0,0],brr[0:])
  
 return subt
function10()


# In[62]:


def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = np.subtract(brr[0:,0:], arr[0:1])
  
    return subt
function10()


# In[71]:


arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
brr = np.array([1,2,3])
subt = np.subtract(brr[0], arr[0:1])


# In[40]:


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([2,3,5])

c= A-b[:,None]

print(c)


# In[70]:


def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([3,3,3])
    brr = np.array([1,2,3])
    subt = np.subtract(brr, arr)
  
    return subt
function10()


# In[95]:


# Task no 11

    # Replace all odd numbers in arr with -1 without changing arr.
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 != 0] = -1
arr


# In[16]:


# Task no 12

# Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking conceptarr = np.array([1,2,3])
arr = np.array([1,2,3])

a = np.repeat(arr,3)
b = np.tile(arr,3)

np.block([a,b])


# In[114]:


# Task no 13

# Set a condition which gets all items between 5 and 10 from arr.

arr = np.array([2, 6, 1, 9, 10, 3, 27])
newArr = arr[(arr > 5) & (arr < 10)]
newArr


# In[109]:


# Task no 14

# Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    
arr = np.arange(10,34,1).reshape((8,3))
np.split(arr,4)


# In[100]:


# Task no 15

#Sort following NumPy array by the second column

arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
arr[np.argsort(arr[:,1])]


# In[97]:


# Task no 16

#Write a NumPy program to join a sequence of arrays along depth.

x = np.array([[1], [2], [3]])
y = np.array([[2], [3], [4]])
np.dstack((x,y))


# In[ ]:





# In[ ]:


#Task17
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    return           # Write Your Code HERE

#Excpected Out
"""
array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
       ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
      dtype='<U3')
"""


# In[126]:


# Task no 17
# replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    
arr = np.arange(1,10*10+1).reshape((10,10))

np.where(arr%3 == 0, 'Yes','No')


# In[9]:


# Task no 18 

    # count values of "students" are exist in "piaic"
    
piaic = np.arange(100)
students = np.array([5,20,50,200,301,7001])
np.count_nonzero(students < 100)


# In[25]:


# Task no 19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X =   np.arange(1,26).reshape(5,5)
    W =   np.transpose(X) 
    b =   5
    output =    (X*W)+b
    return output
function19()
   


# In[13]:


#Task no 20

#apply fuction "abc" on each value of Array "X"x = np.arange(1,11)

x = np.arange(1,11)   
def abc(x):
    arr = x*2+3-2
    return arr
abc(x)

