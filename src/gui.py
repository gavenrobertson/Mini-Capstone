import PySimpleGUI as sg

def intro_window():
    layout = [
        [sg.Text('Welcome, please enter the below information!')],
        [sg.Text('Name: '), sg.Input(key='-NAME-')],
        [sg.Text('Email: '), sg.Input(key='-EMAIL-')],
        [sg.Text('Phone #: '), sg.Input(key='-INTRO_NUMBER-')],
        [sg.Text('Rank: '), sg.Input(key='-RANK-')],
        [sg.Text('DoD ID: '), sg.Input(key='-DOD_ID-')],
        [sg.Button('Next'), sg.Button('Exit')]
    ]
    return sg.Window('My PySimpleGUI App', layout)

def student_window():
    layout = [
        [sg.Text('Welcome, please enter the below information!')],
        [sg.Text('Last Name, First Name: '), sg.Input(key='-LASTFIRST-')],
        [sg.Text('Phone #: '), sg.Input(key='-PHONE-')],
        [sg.Text('Room #: '), sg.Input(key='-ROOM-')],
        [sg.Radio('Pov', 'TRANSPORTATION', key='-POV-')],
        [sg.Radio('Airplane', 'TRANSPORTATION', key='-AIRPLANE-')],
        [sg.Radio('Bus', 'TRANSPORTATION', key='-BUS-')],
        [sg.Radio('Train', 'TRANSPORTATION', key='-TRAIN-')],
        #Need to add user input to specify here
        [sg.Radio('Other', 'TRANSPORTATION', key='-OTHER-')],
        [sg.Text('Departure Date: '), sg.Input(key='-DEPARTURE_DATE-')],
        [sg.Text('Arrival point: '), sg.Input(key='-ARRIVAL_ONE-')],
        [sg.Text('Length of rest: '), sg.Input(key='-LOR_ONE-')],
        [sg.Text('Mileage: '), sg.Input(key='-MILEAGE_ONE-')],
        [sg.Text('Date: '), sg.Input(key='-DATE_TWO-')],
        [sg.Text('Length of rest: '), sg.Input(key='-LOR_TWO-')],
        [sg.Text('Name: '), sg.Input(key='-OTHER_NAME-')],
        [sg.Text('Address: '), sg.Input(key='-ADDRESS-')],
        [sg.Text('Phone Number: '), sg.Input(key='-OTHER_NUMBER-')],
        [sg.Text('Confirmation Number: '), sg.Input(key='-CONFIRMATION_NUMBER-')],
        [sg.Radio('Hotel/Rental', 'TYPE', key='-HOTEL_RENTAL-')],
        [sg.Radio('Residence', 'TYPE', key='-RESIDENCE-')],
        [sg.Radio('Camp Site', 'TYPE', key='-CAMP_SITE-')],
        [sg.Text('Name: '), sg.Input(key='-VISIT_NAME_ONE-')],
        [sg.Text('Number: '), sg.Input(key='-VISIT_NUMBER_ONE-')],
        [sg.Text('Relationship: '), sg.Input(key='-VISIT_RELATIONSHIP_ONE-')],
        [sg.Text('Name: '), sg.Input(key='-VISIT_NAME_TWO-')],
        [sg.Text('Number: '), sg.Input(key='-VISIT_NUMBER_TWO-')],
        [sg.Text('Relationship: '), sg.Input(key='-VISIT_RELATIONSHIP_TWO-')],
        [sg.Text('Instructor Recommendation:')],
        [sg.Radio('Yes', 'INSTRUCTOR', key='-INSTRUCTOR_YES-')],
        [sg.Radio('No', 'INSTRUCTOR', key='-INSTRUCTOR_NO-')],
        [sg.Radio('AFI', 'TYPINSTRUCTORE', key='-AFI-')],
        [sg.Text('Signature'), sg.Input(key='-INSTRUCTOR_SIGNATURE-')],
        [sg.Text('Date: '), sg.Input(key='-INSTRUCTOR_DATE-')],
        [sg.Text('MTL Recommendation:')],
        [sg.Radio('Yes', 'MTL', key='-MTL_YES-')],
        [sg.Radio('No', 'MTL', key='-MTL_NO-')],
        [sg.Text('Signature'), sg.Input(key='-MTL_SIGNATURE-')],
        [sg.Text('Date: '), sg.Input(key='-MTL_DATE-')],
        [sg.Radio('Yes', 'DISTANCE', key='-DISTANCE_YES-')],
        [sg.Radio('No', 'DISTANCE', key='-DISTANCE_NO-')],
        [sg.Text('Circumstance: '), sg.Input(key='-CIRCUMSTANCE-')],
        [sg.Radio('Approved', 'COMMANDER', key='-COMMANDER_APPROVED-')],
        [sg.Radio('Disapproved', 'COMMANDER', key='-COMMANDER_DISAPPROVED-')],
        [sg.Text('Signature'), sg.Input(key='-COMMANDER_SIGNATURE-')],
        [sg.Text('Date: '), sg.Input(key='-COMMANDER_DATE-')],
        [sg.Text('Signature'), sg.Input(key='-STUDENT_SIGNATURE-')],
        [sg.Radio('E1', 'GRADE', key='-E1-')],
        [sg.Radio('E2', 'GRADE', key='-E2-')],
        [sg.Radio('E3', 'GRADE', key='-E3-')],
        [sg.Radio('E4', 'GRADE', key='-E4-')],
        [sg.Text('Date briefed: '), sg.Input(key='-DATE_BRIEFED-')],
        [sg.Text('Briefed by: '), sg.Input(key='-BRIEFED_BY-')],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]
    return sg.Window('4392 Request: ', layout)