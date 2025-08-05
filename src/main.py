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
                event, stu_values = student_view.read()
                if event in (sg.WINDOW_CLOSED, 'Exit'):
                    student_view.close()
                    break

                elif event == 'Submit':
                    more = stu_values['-MORE-']
                    plus = stu_values['-PLUS-']
                    last_first = stu_values['-LASTFIRST-']
                    phone = stu_values['-PHONE-']
                    room = stu_values['-ROOM-']

                    # Transportation radio buttons
                    if stu_values['-POV-']:
                        transportation = 'POV'
                    elif stu_values['-AIRPLANE-']:
                        transportation = 'Airplane'
                    elif stu_values['-BUS-']:
                        transportation = 'Bus'
                    elif stu_values['-TRAIN-']:
                        transportation = 'Train'
                    elif stu_values['-OTHER-']:
                        transportation = 'Other'
                    else:
                        transportation = None

                    departure_date = stu_values['-DEPARTURE_DATE-']
                    arrival_one = stu_values['-ARRIVAL_ONE-']
                    lor_one = stu_values['-LOR_ONE-']
                    mileage_one = stu_values['-MILEAGE_ONE-']
                    date_two = stu_values['-DATE_TWO-']
                    lor_two = stu_values['-LOR_TWO-']
                    other_name = stu_values['-OTHER_NAME-']
                    address = stu_values['-ADDRESS-']
                    other_number = stu_values['-OTHER_NUMBER-']
                    confirmation_number = stu_values['-CONFIRMATION_NUMBER-']

                    # Lodging type radio buttons
                    if stu_values['-HOTEL_RENTAL-']:
                        lodging_type = 'Hotel/Rental'
                    elif stu_values['-RESIDENCE-']:
                        lodging_type = 'Residence'
                    elif stu_values['-CAMP_SITE-']:
                        lodging_type = 'Camp Site'
                    else:
                        lodging_type = None

                    visit_name_one = stu_values['-VISIT_NAME_ONE-']
                    visit_number_one = stu_values['-VISIT_NUMBER_ONE-']
                    visit_relationship_one = stu_values['-VISIT_RELATIONSHIP_ONE-']
                    visit_name_two = stu_values['-VISIT_NAME_TWO-']
                    visit_number_two = stu_values['-VISIT_NUMBER_TWO-']
                    visit_relationship_two = stu_values['-VISIT_RELATIONSHIP_TWO-']
                    
                    
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