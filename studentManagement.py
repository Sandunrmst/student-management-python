
class Students:

    def __init__(self, name, grade, cls, marks):

        self.name = name
        self.grade = grade
        self.cls = cls
        self.marks = marks

    # method for fing each student average mark for given term
    def average_marks(self, term):
        return sum(self.marks[term].values()) / len(self.marks[term])

    # method for fing each student lowest science mark for given term
    def science_marks_for_term(self, term):
        return self.marks[term]['Science']

    def display_student(self):
        print("Name: ", self.name)
        print("Grade: ", self.grade)
        print("Class Room: ", self.cls)
        print("Marks of Terms: ", self.marks)

    # This part help to retrieve the individual propertice of the student object outside of the class
    def student_details(self, info):
        value = ''
        info.lower()
        if info == 'name':
            value = self.name or None
        elif info == 'grade':
            value = self.grade
        elif info == 'classs':
            value = self.cls
        elif info == 'marks':
            value = self.marks
        else:
            pass

        return value


# for store student details in temporary memory
students = []

# In group of student find max average marks for given term


def find_max_average_marks(term):

    max_average_mark = -1
    student_max_average_marks = None
    for student in students:
        avrage_marks = student.average_marks(term)
        if avrage_marks > max_average_mark:
            max_average_mark = avrage_marks
            student_max_average_marks = student
    return student_max_average_marks

# In group of student find lowest science marks for given term


def find_student_lowest_science_marks(term):
    lowest_science_marks = 100
    student_lowest_science_marks = None
    for student in students:
        min_science_marks = student.science_marks_for_term(term)
        if min_science_marks < lowest_science_marks:
            lowest_science_marks = min_science_marks
            student_lowest_science_marks = student
    return student_lowest_science_marks

# Main body of the funtion


def run_system():
    while True:
        print("Please Enter Number You need to proceed\n")
        print("1. Enter Student Details ")
        print("2. Display Students with details ")
        print("3. Display who has the Maximum Average Marks for Given Term")
        print("4. Display who has the lowest science Mark for Given Term")
        print("5. For Exit\n")
        user_input = int(input("Enter your Choice: "))

        if user_input == 1:
            while True:
                print("Stop adding Student enter '#'")
                print("For continue adding student enter '$'\n")
                end = input("Enter your choice: \n")
                if end == '$':
                    name = input("Enter Student Name: ")
                    grade = int(input("Enter Student Grade: "))
                    cls = input("Enter Student Class Room: ")
                    student_marks = {}
                    for i in range(1, 4):
                        print(f"Enter Term {i} Marks: ")
                        maths_marks = int(input("Enter Maths Marks: "))
                        science_marks = int(input("Enter Science Marks: "))
                        art_marks = int(input("Enter Art Marks: "))

                        student_marks[f"Term {i}"] = {
                            'Maths': maths_marks,
                            'Science': science_marks,
                            'Art': art_marks,
                        }
                    students.append(Students(name, grade, cls, student_marks))
                elif end == '#':
                    print("Adding completed")
                    break
                else:
                    print("Please input valid symbol -> '#' '$' ")

        elif user_input == 2:

            count = 1
            for student in students:
                print("")
                print(f"Student {count}")
                student.display_student()
                count = count + 1

        elif user_input == 3:
            number = input("Enter Term number 1 to 3: ")
            number = f"Term {number}"

            maximum_average_marks = find_max_average_marks(number)
            student_info = maximum_average_marks

            print(f"Student Name: {student_info.student_details('name')}")
            print(f"Grade: {student_info.student_details('grade')}")
            print(
                f"Maximum Average Marks: {student_info.average_marks(number)}")

        elif user_input == 4:
            number = input("Enter term number 1 to 3: ")
            number = f"Term {number}"

            lowest_science_marks = find_student_lowest_science_marks(number)
            student_info = lowest_science_marks

            print(f"Student Name: {student_info.student_details('name')}")
            print(f"Grade: {student_info.student_details('name')}")

            marks = student_info.student_details('marks')
            print(f"Science Mark:{marks[number]['Science']} ")

        elif user_input == 5:
            print("Thank you for working with our Student Management System")
            exit()
        else:
            print("Please enter valid input 1 to 5")


# Call the main funtion to run this system
run_system()
