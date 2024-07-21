# dictionary example 
student={'hindi':78,'english':89,'standard':'10th','stdname':'Anuj Singh'}
# print(student)


# student.pop('english')
# it will delete the element which has the key of english 
# print(student)


# student.popitem()
# it will delete the element  from the dictionary last position
# print(student)


# dictionary.key() method : it will used to fetch the dictionary key 
name = student.keys()
# print(name)


# Dictionary.values() method : it will used to fetch the dictionary values
value = student.values()
# print(value)


# dictionary.items() method : return a list item from dictionary (key, value)
item = student.items()
# print(item)


k = student.get('hindi')
# print(k)



dictobj1 = {'hindi':78,'english':89,'standard':'10th','stdname':'Anuj Singh'}
dictobj2 = {'hindi':78,'english':80,'standard':'9th','stdname':'Aniket'}
dictobj1.update(dictobj2)
print(dictobj1.items())
