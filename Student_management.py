students=[]

def add_student():
    roll_no= int(input("Enter the student roll number"))
    name = input("Enter the Student name")
    course = input("Enter the students course")

    student={
        "roll_no": roll_no,
        "name": name,
        "course": course
    }

    students.append(student)

    print(f'student {name} added successfully!')

def Display():
    if len(students)==0:
        print("No student to display")

    else:
        print("Student details:\n")
        for s in students:
            print(
                f"Roll Number:{s['roll_no']},Name:{s['name']}, Course:{s['course']}, "
            )


def Search():
    roll_no=input("Enter the roll number")

    found = False
    for s in students:
        if s['roll_no']== roll_no:
            print(
                f"Roll Number:{s['roll_no']},Name:{s['name']}, Course:{s['course']}, "
            )
            found=True
            break

        if not found:
            print(f'there is no student with roll no {roll_no}')


while True:
    print("Student management\n")

    print("Press 1 to add student\n ")

    print("Press 2 to Display all student\n")

    print("Press 3 to search\n")

    print("Press 4 to exit\n")

    c = int(input("Enter your choice\n"))

    if c==1:
        add_student()

    elif c==2:
        Display()

    elif c==3:
        Search()

    elif c==4:
        print("Exiting the program")
        break

    else:
        print("Invalid choice enter again")

        