import PySimpleGUI as sg
import csv
from gui import intro_window, student_window
from app import Mil, Mtl, Student, Instructor, FortyThree92

def main():
    intro_view = intro_window()

    while True:
        event, values = intro_view.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            intro_view.close()
            break

        elif event == 'Next':
            # Extract data from intro window
            dod_id = "1234567890"  
            name = values['-NAME-']
            rank = values['-RANK-']
            email = values['-EMAIL-']
            squad = "336"     
            phonenumber = '12345612345'
            instructor_assigned = 'Mr. Lee'

            # Create Student object
            new_Student = Student(dod_id, name, rank, email, squad, phonenumber, instructor_assigned)


            # Now open student window
            intro_view.close()
            student_view = student_window()

            while True:
                event, fortythree92_values = student_view.read()
                if event in (sg.WINDOW_CLOSED, 'Exit'):
                    student_view.close()
                    break

                elif event == 'Submit':
                    more = stu_values['-MORE-']
                    plus = stu_values['-PLUS-']

                    
                    student = Student(
                        dod_id="S789012",
                        name="Student Name",
                        rank="Trainee",
                        email="student@example.com",
                        squad=plus,
                        phonenumber=more,
                        instructor=instructor
                    )

                    instructor.add_stu(student)

                    # Debug print
                    print(f"Instructor: {instructor.name}, Student: {student.phonenumber}, {student.squad}")
                    
                    student_view.close()
                    break
            break

def intialize_teachers():
    list_of_students = []
    with open('assets/data/teacher.csv', 'r', newline='') as teachers_students:
        csv_output = csv.reader(teachers_students)
        for line in csv_output:
            if line:
                list_of_students.append(line)

    return list_of_students

if __name__ == '__main__':
    main()