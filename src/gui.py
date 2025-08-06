import PySimpleGUI as sg

def intro_window():
    #User input for intro window, creates data for Student object
    layout = [
        [sg.Text('Welcome, please enter the below information!')],
        [sg.Text('Name: '), sg.Input(key='-NAME-', size=(20, 10))],
        [sg.Text('Email: '), sg.Input(key='-EMAIL-', size=(30, 1))],
        [sg.Text('Phone #: '), sg.Input(key='-INTRO_NUMBER-', size=(20, 1))],
        [sg.Text('Rank: '), sg.Input(key='-RANK-', size=(20, 1))],
        [sg.Text('DoD ID: '), sg.Input(key='-DOD_ID-', size=(20, 1))],
        [sg.Button('Next'), sg.Button('Exit')]
    ]
    return sg.Window('My PySimpleGUI App', layout, size=(350, 170))

def student_window(new_Student):
    #User input for 4392 form, creates data for 4392 object
    layout = [
        [sg.Text('Welcome, please enter the below information!')],
        [sg.Text('Last Name, First Name: '), sg.Input(key='-LASTFIRST-', size=(20, 1), default_text=new_Student.name), sg.Text('Phone #: '), sg.Input(key='-PHONE-', size=(20, 1), default_text=new_Student.phonenumber), sg.Text('Room #: '), sg.Input(key='-ROOM-', size=(20, 1), default_text='260')],
        [sg.Text('Mode of Transportation:')],
        [sg.Radio('Pov', 'TRANSPORTATION', key='-POV-'), sg.Radio('Airplane', 'TRANSPORTATION', key='-AIRPLANE-'), sg.Radio('Bus', 'TRANSPORTATION', key='-BUS-'), sg.Radio('Train', 'TRANSPORTATION', key='-TRAIN-'), sg.Radio('Other', 'TRANSPORTATION', key='-OTHER-')],
        [sg.Text('Departure point: '), sg.Input(key='-DEPARTURE_DATE-', size=(20, 1), default_text='Keesler AFB')],
        [sg.Text('Arrival point: '), sg.Input(key='-ARRIVAL_ONE-', size=(20, 1))],
        [sg.Text('Length of rest: '), sg.Input(key='-LOR_ONE-', size=(20, 1))],
        [sg.Text('Mileage: '), sg.Input(key='-MILEAGE_ONE-', size=(20, 1))],
        [sg.Text('Date: '), sg.Input(key='-DATE_TWO-', size=(10, 1))],
        [sg.Text('Length of rest: '), sg.Input(key='-LOR_TWO-', size=(20, 1))],
        [sg.Text('Name: '), sg.Input(key='-OTHER_NAME-', size=(20, 1))],
        [sg.Text('Address: '), sg.Input(key='-ADDRESS-', size=(20, 1))],
        [sg.Text('Phone Number: '), sg.Input(key='-OTHER_NUMBER-', size=(20, 1))],
        [sg.Text('Confirmation Number: '), sg.Input(key='-CONFIRMATION_NUMBER-', size=(20, 1))],
        [sg.Radio('Hotel/Rental', 'TYPE', key='-HOTEL_RENTAL-'), sg.Radio('Residence', 'TYPE', key='-RESIDENCE-'), sg.Radio('Camp Site', 'TYPE', key='-CAMP_SITE-')],
        [sg.Text('Name: '), sg.Input(key='-VISIT_NAME_ONE-', size=(20, 1)), sg.Text('Number: '), sg.Input(key='-VISIT_NUMBER_ONE-', size=(20, 1)), sg.Text('Relationship: '), sg.Input(key='-VISIT_RELATIONSHIP_ONE-', size=(20, 1))],
        [sg.Text('Name: '), sg.Input(key='-VISIT_NAME_TWO-', size=(20, 1)), sg.Text('Number: '), sg.Input(key='-VISIT_NUMBER_TWO-', size=(20, 1)), sg.Text('Relationship: '), sg.Input(key='-VISIT_RELATIONSHIP_TWO-', size=(20, 1))],
        [sg.Text('Student Signature'), sg.Input(key='-STUDENT_SIGNATURE-')],
        [sg.Text('Grade: '), sg.Radio('E1', 'GRADE', key='-E1-'), sg.Radio('E2', 'GRADE', key='-E2-'), sg.Radio('E3', 'GRADE', key='-E3-'), sg.Radio('E4', 'GRADE', key='-E4-')],
        [sg.Text('Date briefed: '), sg.Input(key='-DATE_BRIEFED-', size=(10, 1))],
        [sg.Text('Briefed by: '), sg.Input(key='-BRIEFED_BY-')],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]

    #     layout = [
    #     [sg.Text('Welcome, please enter the below information!')],
    #     [sg.Text('Last Name, First Name: '), sg.Input(key='-LASTFIRST-', size=(20, 1)), sg.Text('Phone #: '), sg.Input(key='-PHONE-', size=(20, 1)), sg.Text('Room #: '), sg.Input(key='-ROOM-', size=(20, 1))],
    #     [sg.Text('Mode of Transportation:')],
    #     [sg.Radio('Pov', 'TRANSPORTATION', key='-POV-'), sg.Radio('Airplane', 'TRANSPORTATION', key='-AIRPLANE-'), sg.Radio('Bus', 'TRANSPORTATION', key='-BUS-'), sg.Radio('Train', 'TRANSPORTATION', key='-TRAIN-'), sg.Radio('Other', 'TRANSPORTATION', key='-OTHER-')],
    #     [sg.Text('Departure Date: '), sg.Input(key='-DEPARTURE_DATE-', size=(10, 1))],
    #     [sg.Text('Arrival point: '), sg.Input(key='-ARRIVAL_ONE-', size=(20, 1))],
    #     [sg.Text('Length of rest: '), sg.Input(key='-LOR_ONE-', size=(20, 1))],
    #     [sg.Text('Mileage: '), sg.Input(key='-MILEAGE_ONE-', size=(20, 1))],
    #     [sg.Text('Date: '), sg.Input(key='-DATE_TWO-', size=(10, 1))],
    #     [sg.Text('Length of rest: '), sg.Input(key='-LOR_TWO-', size=(20, 1))],
    #     [sg.Text('Name: '), sg.Input(key='-OTHER_NAME-', size=(20, 1))],
    #     [sg.Text('Address: '), sg.Input(key='-ADDRESS-', size=(20, 1))],
    #     [sg.Text('Phone Number: '), sg.Input(key='-OTHER_NUMBER-', size=(20, 1))],
    #     [sg.Text('Confirmation Number: '), sg.Input(key='-CONFIRMATION_NUMBER-', size=(20, 1))],
    #     [sg.Radio('Hotel/Rental', 'TYPE', key='-HOTEL_RENTAL-'), sg.Radio('Residence', 'TYPE', key='-RESIDENCE-'), sg.Radio('Camp Site', 'TYPE', key='-CAMP_SITE-')],
    #     [sg.Text('Name: '), sg.Input(key='-VISIT_NAME_ONE-', size=(20, 1)), sg.Text('Number: '), sg.Input(key='-VISIT_NUMBER_ONE-', size=(20, 1)), sg.Text('Relationship: '), sg.Input(key='-VISIT_RELATIONSHIP_ONE-', size=(20, 1))],
    #     [sg.Text('Name: '), sg.Input(key='-VISIT_NAME_TWO-', size=(20, 1)), sg.Text('Number: '), sg.Input(key='-VISIT_NUMBER_TWO-', size=(20, 1)), sg.Text('Relationship: '), sg.Input(key='-VISIT_RELATIONSHIP_TWO-', size=(20, 1))],
    #     [sg.Text('Instructor Recommendation:')],
    #     [sg.Radio('Yes', 'INSTRUCTOR', key='-INSTRUCTOR_YES-'), sg.Radio('No', 'INSTRUCTOR', key='-INSTRUCTOR_NO-'), sg.Radio('AFI', 'TYPINSTRUCTORE', key='-AFI-'), sg.Text('Date: '), sg.Input(key='-INSTRUCTOR_DATE-', size=(10, 1))],
    #     [sg.Text('MTL Recommendation:')],
    #     [sg.Radio('Yes', 'MTL', key='-MTL_YES-'), sg.Radio('No', 'MTL', key='-MTL_NO-'), sg.Text('Date: '), sg.Input(key='-MTL_DATE-', size=(10, 1))],
    #     [sg.Radio('Yes', 'DISTANCE', key='-DISTANCE_YES-'), sg.Radio('No', 'DISTANCE', key='-DISTANCE_NO-')],
    #     [sg.Text('Circumstance: '), sg.Input(key='-CIRCUMSTANCE-')],
    #     [sg.Radio('Approved', 'COMMANDER', key='-COMMANDER_APPROVED-'), sg.Radio('Disapproved', 'COMMANDER', key='-COMMANDER_DISAPPROVED-'), sg.Text('Date: '), sg.Input(key='-COMMANDER_DATE-', size=(10, 1))],
    #     [sg.Text('Student Signature'), sg.Input(key='-STUDENT_SIGNATURE-')],
    #     [sg.Text('Grade: '), sg.Radio('E1', 'GRADE', key='-E1-'), sg.Radio('E2', 'GRADE', key='-E2-'), sg.Radio('E3', 'GRADE', key='-E3-'), sg.Radio('E4', 'GRADE', key='-E4-')],
    #     [sg.Text('Date briefed: '), sg.Input(key='-DATE_BRIEFED-', size=(10, 1))],
    #     [sg.Text('Briefed by: '), sg.Input(key='-BRIEFED_BY-')],
    #     [sg.Button('Submit'), sg.Button('Exit')]
    # ]

    
    return sg.Window('4392 Request: ', layout)