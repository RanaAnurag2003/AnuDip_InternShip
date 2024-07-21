file = open("test.txt",'w')

# if file:
#     print("file created successfully")
# else:
#     print("file not created successfully")


file.write("welcome to text file welcome to text filewelcome to text filewelcome to text filewelcome to text filewelcome to text filewelcome to text filewelcome to text filewelcome to text filewelcome to text filewelcome to text file")

# file.close()



# with statement
# with open("test1.txt",'w') as test_file:
#     test_file.write(" hello world world ")


# with open("test.txt",'r') as test_file:
#     data =test_file.read()
#     print(data)

file = open("test.txt",'r')
# print(file.tell())
data = file.read(10)
# print(file.tell())
# print(data)
# file.close()



# Searching data in file 
file_path = "C:\\Users\\aj\Documents\\Data visualization\\test.txt"
# print(file_path)

# search_keyword= input("Enter the txt which you wnat to search")
# with open(file_path,'r') as file2:
#     for line in file2 :
#         if search_keyword.lower() in line.lower():
#             print(line.strip())

# print(f"Search for'{search_keyword}' completed")




# total number of vowel and consonants in the file

# with open(file_path,'r') as file1:
