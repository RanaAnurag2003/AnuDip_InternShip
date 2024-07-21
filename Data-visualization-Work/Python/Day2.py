# Dictionary
 #!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating a tuple and decalring it 

numbers= (1,2,3,2,32,323,222,232,31232,3)
print(numbers)


# In[2]:


print(*numbers)


# In[4]:


# Accessing each element one by one displaying them 


# In[3]:


for x in range(len(numbers)):
    print(numbers[x])


# In[8]:


# Display element in horizontal way 
for index in range(len(numbers)):
    print(numbers[index],end=", ")


# In[14]:


# Display element of tuple in forward direction using bakward index
for index in range(-len(numbers),0):
    print(numbers[index], end=' ')
print()
print('-------------------------------')  
    
#     Display element of tuple in backward direction using forward index
for index in range(len(numbers)):
    print(numbers[len(numbers)-index-1],end=' ')
    


# In[17]:


# To display the sum of all numbers of tuple 
sum =0
for index in range(len(numbers)):
    sum+=numbers[index]
print("The sum of the all numbers of tuple is : ",sum)


# In[18]:


numbers.sort()

# -------------------------------------------------------------
# In[ ]:
#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dictionary 
student ={'stdid':'std101','maths':78,'stdname':'Ashish Kumar','Age':15}
print("Student Data: ")
print(student)


# In[6]:


for element in student:
    print(element,":",student[element])


# In[7]:


print("Dictionary :",student)


# In[9]:


#  insertion in dictionary 
# to insert an  element with the key maths and value 90
student['maths'] = 90

# to insert an elment with the key english and value is 80
student['english'] = 89
print('-------------------------------------')
print(student)


# In[22]:


# deletion from the dictinary 
student.pop('maths')
print(student)


# In[ ]:





# In[ ]:










