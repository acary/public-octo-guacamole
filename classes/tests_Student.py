from class_Student import Student

# Instantiate class with 5 students
student0 = Student("Alan", 29, 4.0)
student1 = Student("Benji", 27, 2.0)
student2 = Student("Dave", 29, 3.4)
student3 = Student("Dave", 29, 3.4)
student4 = Student("Edgar", 23, 3.1)

# Create test array of 5 students
student_array = [student0, student1, student2, student3, student4]

print("\n")
print("Initialized student array...\n")

# Demonstrates method: __str__
print("Demonstrates method: __str__")
print(str(student0))
print(str(student1))
print(str(student2))
print(str(student3))
print(str(student4))
print("\n")

# Demonstrates method: __lt__
print("Demonstrates method: __lt__")
print(student0.__lt__(student1))
print(student1.__lt__(student4))
print(student2.__lt__(student1))
print(student3.__lt__(student2))
print(student4.__lt__(student3))
print("\n")

# Demonstrates method: __eq__
print("Demonstrates method: __eq__")
print(student0.__eq__(student1))
print(student1.__eq__(student4))
print(student2.__eq__(student3))
print(student3.__eq__(student2))
print(student4.__eq__(student3))
print("\n")

# Demonstrates method: __hash__
print("Demonstrates method: __hash__")
print(student0.__hash__())
print(student1.__hash__())
print(student2.__hash__())
print(student3.__hash__())
print(student4.__hash__())
print("\n")

# (b) Write test code that exercises these methods using sorted() and dict()
# Test 1:
def myFn(s):
    return s.gpa

print("[Test 1] Returns students by lowest to highest GPA using sorted():")
test1 = sorted(student_array, key=myFn)
for student in test1:
    print(student.name + ', ' + str(student.gpa))
print("\n")

# Test 2:
print("[Test 2] Returns students whose GPA is GTE to 3.0 using sorted() and dict():")
dict1 = {}
for student in student_array:
    if student.gpa >= 3.0:
        dict1.update({ student.name: student.gpa})
dict1 = sorted(dict1, reverse=True)
print(dict1)
print("\n")

# Test 3:
print("[Test 3] Determines if student has 4.0 GPA using __hash__():")
list2 = []
for student in student_array:
    if student.gpa == 4.0:
        list2.append(student.__hash__())
for student in student_array:
    if student.__hash__() in list2:
        print(student.name + ' has a perfect GPA!')
print("\n")

# (c) Sort students in order of increasing GPA using a lambda expression
print("[Test 4] Sorts students in order of increasing GPA using a lambda expression:")
test3 = sorted(student_array, key=lambda student: student.gpa)
for lambda_student in test3:
    print(lambda_student.name + ', ' + str(lambda_student.gpa))
print("\n...End of tests")
