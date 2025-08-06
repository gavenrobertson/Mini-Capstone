import PySimpleGUI as sg
import csv
import random
from gui import intro_window, student_window
from app import Mtl, Student, Instructor, FortyThree92
from faker import Faker #found this helpful for making fake data.

#Theme
sg.theme('DarkBlue1')

def main():
    """
    Main function to run student side of application.
    """

    #Launch the intro window
    intro_view = intro_window()

    #Initialize the instructor and MTL objects
    the_instructor = Instructor(9835472, 'Mr. Lee', 'CIV', 'mrlee@stellaris.com', 336, intialize_teachers())
    the_mtl = Mtl(1236482, 'SSgt Blakley', 'E5', 'sgtblakley@us.af.mil', 336)

    print(the_instructor)
    print(the_mtl)

    while True:
        event, values = intro_view.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            intro_view.close()
            break

        elif event == 'Next':
            # Extract data from intro window
            dod_id = values['-DOD_ID-']
            name = values['-NAME-']
            rank = values['-RANK-']
            email = values['-EMAIL-']
            squad = "336"     
            phonenumber = values['-INTRO_NUMBER-']
            instructor_assigned = the_instructor.name

            # Create Student object
            new_Student = Student(dod_id, name, rank, email, squad, phonenumber, instructor_assigned)
    

            print(new_Student)

            # Now open student window
            intro_view.close()
            student_view = student_window(new_Student)

            #Main loop for student window
            while True:
                event, stu_values = student_view.read()
                if event in (sg.WINDOW_CLOSED, 'Exit'):
                    student_view.close()
                    break
                #taking in from the user and then setting values to the variables
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
                    
                    file_path = "assets/data/form_4392_full.csv"

                    create_4392_objects()
                    
                    # Save the form data to CSV
                    with open(file_path, "a", newline="") as file:
                        writer = csv.writer(file)
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

#this assings the students in the csv to the teachers
def intialize_teachers():
    """
    Reads the teacher's CSV file and returns a list of students assigned to each teacher.
    """
    list_of_students = []
    with open('assets/data/teacher.csv', 'r', newline='') as teachers_students:
        csv_output = csv.reader(teachers_students)
        for line in csv_output:
            if line:
                list_of_students.append(line)

    return list_of_students

# Function to create 4392 objects and save to CSV
def create_4392_objects():
    """
    Appends 10 random FortyThree92 objects to the CSV file and writes header row if file is empty.
    """
    fake = Faker()
    with open("assets/data/form_4392_full.csv", "a", newline="") as file:
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
        for _ in range(10):
            f = FortyThree92(
                name=fake.name(),
                phonenumber=fake.phone_number(),
                room=str(random.randint(100, 999)),
                transportation=random.choice(["POV", "Bus", "Air", "Train"]),
                departure_date=str(fake.date_between(start_date="-30d", end_date="today")),
                arrival_one=fake.city(),
                lor_one=str(random.randint(1, 5)),
                mileage_one=str(random.randint(10, 1000)),
                date_two=str(fake.date_between(start_date="today", end_date="+30d")),
                lor_two=str(random.randint(1, 5)),
                other_name=fake.name(),
                address=fake.address().replace('\n', ', '),
                other_number=fake.phone_number(),
                confirmation_number=str(random.randint(100000, 999999)),
                lodging_type=random.choice(["Hotel", "Residence", "Other"]),
                visitor1_name=fake.name(),
                visitor1_number=fake.phone_number(),
                visitor1_relationship=random.choice(["Friend", "Family", "Spouse"]),
                visitor2_name=fake.name(),
                visitor2_number=fake.phone_number(),
                visitor2_relationship=random.choice(["Friend", "Family", "Spouse"]),
                student_signature=fake.name(),
                grade=random.choice(["E1", "E2", "E3", "E4"]),
                date_briefed=str(fake.date_this_month()),
                briefed_by=fake.name()
            )
            
            writer.writerow([
                f.name,
                f.phonenumber,
                f.room,
                f.transportation,
                f.departure_date,
                f.arrival_one,
                f.lor_one,
                f.mileage_one,
                f.date_two,
                f.lor_two,
                f.other_name,
                f.address,
                f.other_number,
                f.confirmation_number,
                f.lodging_type,
                f.visitor1_name,
                f.visitor1_number,
                f.visitor1_relationship,
                f.visitor2_name,
                f.visitor2_number,
                f.visitor2_relationship,
                f.student_signature,
                f.grade,
                f.date_briefed,
                f.briefed_by,
                f.status
            ])

if __name__ == '__main__':
    main()