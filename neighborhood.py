# Level 1:

# Create a class called Student that has two attributes: a name, and a grade.
class Student:
    def __init__(self, this_students_name, this_students_grade):
        self.name = this_students_name
        self.grade = this_students_grade

# Now create instances of three different students (student1, student2, and student3).
student1 = Student("Diego","86")
student2 = Student("Bernard","73")
student3 = Student("Bob", "35") 

# Confirm that the class works by printing out the first student's name.
print(student1.name)


# Level 2:

# Create a class called School that has three attributes: a name, a type, and a size.
class School:
    def __init__(self, this_schools_name, this_schools_type, this_schools_size):
        self.name = this_schools_name
        self.type = this_schools_type
        self.size = this_schools_size

# Create instances of three individual schools.
school1 = School("MBHS", "High", 650)
school2 = School("Stuy", "High", 3000)
school3 =School("FintechFocus", "Summer", 80)

# Confirm that the class works by printing out the name and size of the third school.
print(school1.size)
print(school2.type)

# Level 3:


# Create a class called House that has four attributes: an address, a size, a price, and a number of bedrooms.
class House:
    def __init__(self, address, size, price, bedrooms):
        self.address= address
        self.size= size
        self.price= price 
        self.bedrooms= bedrooms

# Create instances of at least three individual houses.
house1= House("4 Street",800, 40000000, 2)

# Confirm that the class works by printing out the address and size of the second house.
print(house1.address)

# Level 4: (Stretch)


# Put your three students in a list called my_students, your houses in a list for houses, and your schools in a list for schools.
my_students= [Student1, student2, student3]

# Iterate over the student list, printing out "_____ is in grade __." For each of the students.
# Iterate over the houses list and print out a description for each one. Do the same for your schools lists.
# Level 5: (Stretch)
# Modify your student class above to include a savings_account value for each student. Change your initializers so that the code still runs. 
# Write some code that compares a student and a house, and determines whether or not the student can afford to buy the house.