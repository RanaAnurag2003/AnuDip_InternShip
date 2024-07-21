students = [
  {"stdid": "std101", "stdname": "Ashish kumar", "standard": "10th", "Age": 15, "Hindi": 67, "English": 89, "Math": 87, "Science": 89, "Computer": 90, "Total": 422},
  {"stdid": "std102", "stdname": "Abhishek kumar", "standard": "10th", "Age": 14, "Hindi": 85, "English": 45, "Math": 48, "Science": 90, "Computer": 45, "Total": 313},
  {"stdid": "std103", "stdname": "Aman", "standard": "10th", "Age": 15, "Hindi": 23, "English": 56, "Math": 78, "Science": 78, "Computer": 67, "Total": 302},
  {"stdid": "std104", "stdname": "Rahul", "standard": "10th", "Age": 14, "Hindi": 45, "English": 67, "Math": 45, "Science": 45, "Computer": 56, "Total": 258},
  {"stdid": "std105", "stdname": "Ruby", "standard": "10th", "Age": 13, "Hindi": 89, "English": 67, "Math": 89, "Science": 93, "Computer": 65, "Total": 402},
  {"stdid": "std106", "stdname": "Suman", "standard": "10th", "Age": 13, "Hindi": 90, "English": 46, "Math": 67, "Science": 67, "Computer": 67, "Total": 337},
  {"stdid": "std107", "stdname": "Saurabh", "standard": "10th", "Age": 15, "Hindi": 45, "English": 23, "Math": 34, "Science": 45, "Computer": 34, "Total": 181},
  {"stdid": "std108", "stdname": "Sumit", "standard": "10th", "Age": 14, "Hindi": 23, "English": 45, "Math": 67, "Science": 78, "Computer": 90, "Total": 303},
  {"stdid": "std109", "stdname": "Kamlesh", "standard": "10th", "Age": 15, "Hindi": 45, "English": 56, "Math": 78, "Science": 99, "Computer": 67, "Total": 345},
  {"stdid": "std110", "stdname": "Rohan", "standard": "10th", "Age": 15, "Hindi": 34, "English": 12, "Math": 24, "Science": 45, "Computer": 56, "Total": 171}
]

print(students[0].keys())
for i in range(len(students)):
    print(students[i].values())

print('----------------------------------------------------------------')
# First task: Display the name of student whose marks in English is greater than 50
for student in students:
    if student['English'] > 50:
        print(student['stdname'])


