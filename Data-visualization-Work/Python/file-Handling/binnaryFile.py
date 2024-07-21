import pickle 
file= open("first.dat","wb")
t =[1,2,33,4,44,3,2]
pickle.dump(t,file)
file.close()
print("data loaded") 



f = open("first.dat","rb")
data2 = pickle.load(f)
print(data2)
f.close()


# store the id,name , marks 
# marks greater than 90




