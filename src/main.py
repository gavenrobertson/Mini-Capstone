import PySimpleGUI as sg
import csv
from gui import intro_window, student_window
from app import Mtl, Student, Instructor, FortyThree92

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
                    name = stu_values['-LASTFIRST-']
                    phonenumber = stu_values['-PHONE-']
                    room = stu_values['-ROOM-']

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

                    if stu_values['-HOTEL_RENTAL-']:
                        lodging_type = 'Hotel/Rental'
                    elif stu_values['-RESIDENCE-']:
                        lodging_type = 'Residence'
                    elif stu_values['-CAMP_SITE-']:
                        lodging_type = 'Camp Site'
                    else:
                        lodging_type = None

                    visitor1_name = stu_values['-VISIT_NAME_ONE-']
                    visitor1_number = stu_values['-VISIT_NUMBER_ONE-']
                    visitor1_relationship = stu_values['-VISIT_RELATIONSHIP_ONE-']
                    visitor2_name = stu_values['-VISIT_NAME_TWO-']
                    visitor2_number = stu_values['-VISIT_NUMBER_TWO-']
                    visitor2_relationship = stu_values['-VISIT_RELATIONSHIP_TWO-']

                    student_signature = stu_values['-STUDENT_SIGNATURE-']

                    if stu_values['-E1-']:
                        grade = 'E1'
                    elif stu_values['-E2-']:
                        grade = 'E2'
                    elif stu_values['-E3-']:
                        grade = 'E3'
                    elif stu_values['-E4-']:
                        grade = 'E4'
                    else:
                        grade = None

                    date_briefed = stu_values['-DATE_BRIEFED-']
                    briefed_by = stu_values['-BRIEFED_BY-']

                    
                    try:
                        mileage_one_int = int(mileage_one)
                    except ValueError:
                        mileage_one_int = 0

                    # Create 4392 object
                    form_4392 = FortyThree92(
                        name=name,
                        phonenumber=phonenumber,
                        room=room,
                        transportation=transportation,
                        departure_date=departure_date,
                        arrival_one=arrival_one,
                        lor_one=lor_one,
                        mileage_one=mileage_one_int,
                        date_two=date_two,
                        lor_two=lor_two,
                        other_name=other_name,
                        address=address,
                        other_number=other_number,
                        confirmation_number=confirmation_number,
                        lodging_type=lodging_type,
                        visitor1_name=visitor1_name,
                        visitor1_number=visitor1_number,
                        visitor1_relationship=visitor1_relationship,
                        visitor2_name=visitor2_name,
                        visitor2_number=visitor2_number,
                        visitor2_relationship=visitor2_relationship,
                        student_signature=student_signature,
                        grade=grade,
                        date_briefed=date_briefed,
                        briefed_by=briefed_by
                    )
                    
                    file_path = "form_4392_full.csv"

                    
                    with open(file_path, "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([
                            "Name",
                            "Phone Number",
                            "Room",
                            "Transportation",
                            "Departure Date",
                            "Arrival One",
                            "LOR One",
                            "Mileage One",
                            "Date Two",
                            "LOR Two",
                            "Other Name",
                            "Address",
                            "Other Number",
                            "Confirmation Number",
                            "Lodging Type",
                            "Visitor 1 Name",
                            "Visitor 1 Number",
                            "Visitor 1 Relationship",
                            "Visitor 2 Name",
                            "Visitor 2 Number",
                            "Visitor 2 Relationship",
                            "Student Signature",
                            "Grade",
                            "Date Briefed",
                            "Briefed By",
                            "Status"
                        ])
                        writer.writerow([
                            form_4392.name,
                            form_4392.phonenumber,
                            form_4392.room,
                            form_4392.transportation,
                            form_4392.departure_date,
                            form_4392.arrival_one,
                            form_4392.lor_one,
                            form_4392.mileage_one,
                            form_4392.date_two,
                            form_4392.lor_two,
                            form_4392.other_name,
                            form_4392.address,
                            form_4392.other_number,
                            form_4392.confirmation_number,
                            form_4392.lodging_type,
                            form_4392.visitor1_name,
                            form_4392.visitor1_number,
                            form_4392.visitor1_relationship,
                            form_4392.visitor2_name,
                            form_4392.visitor2_number,
                            form_4392.visitor2_relationship,
                            form_4392.student_signature,
                            form_4392.grade,
                            form_4392.date_briefed,
                            form_4392.briefed_by,
                            form_4392.status
                        ])

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