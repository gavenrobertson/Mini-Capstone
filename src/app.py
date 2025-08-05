class Mil:
    '''
    Represents a generic military personnel.

    Attributes:
        _dod_id (str): Department of Defense ID.
        _name (str): Full name of the personnel.
        _email (str): Email address.
        rank (str): Military rank.
        squad (str): Assigned squad.
    '''
    def __init__(self, dod_id: str, name: str, rank: str, email: str, squad: str):
        '''
        Initializes a Mil object.

        Args:
            dod_id (str): DoD ID.
            name (str): Name of the personnel.
            rank (str): Rank of the personnel.
            email (str): Email of the personnel.
            squad (str): Squad assignment.
        '''
        self._dod_id = dod_id
        self._name = name
        self.rank = rank
        self._email = email
        self.squad = squad

    @property
    def dod_id(self) -> str:
        '''Gets the DoD ID.'''
        return self._dod_id

    @dod_id.setter
    def dod_id(self, new_id: str):
        '''Sets the DoD ID.'''
        self._dod_id = new_id

    @property
    def name(self) -> str:
        '''Gets the name.'''
        return self._name

    @name.setter
    def name(self, new_name: str):
        '''Sets the name.'''
        self._name = new_name

    @property
    def email(self) -> str:
        '''Gets the email.'''
        return self._email

    @email.setter
    def email(self, new_email: str):
        '''Sets the email.'''
        self._email = new_email


class Mtl(Mil):
    '''
    Represents a Military Training Leader (MTL).

    Inherits from:
        Mil
    '''
    def __init__(self, dod_id: str, name: str, rank: str, email: str, squad: str):
        '''
        Initializes an MTL object.

        Args:
            dod_id (str): DoD ID.
            name (str): Name of the MTL.
            rank (str): Rank of the MTL.
            email (str): Email of the MTL.
            squad (str): Assigned squad.
        '''
        super().__init__(dod_id, name, rank, email, squad)

    @property
    def dod_id(self) -> str:
        '''Gets the DoD ID.'''
        return self._dod_id

    @dod_id.setter
    def dod_id(self, new_id: str):
        '''Sets the DoD ID.'''
        self._dod_id = new_id

    @property
    def name(self) -> str:
        '''Gets the name.'''
        return self._name

    @name.setter
    def name(self, new_name: str):
        '''Sets the name.'''
        self._name = new_name

    @property
    def email(self) -> str:
        '''Gets the email.'''
        return self._email

    @email.setter
    def email(self, new_email: str):
        '''Sets the email.'''
        self._email = new_email


class Student(Mil):
    '''
    Represents a student under military instruction.

    Inherits from:
        Mil

    Attributes:
        phonenumber (str): Contact phone number.
        instructor (Instructor): Assigned instructor object.
    '''
    def __init__(self, dod_id: str, name: str, rank: str, email: str, squad: str, phonenumber: str, instructor):
        '''
        Initializes a Student object.

        Args:
            dod_id (str): DoD ID.
            name (str): Name of the student.
            rank (str): Rank of the student.
            email (str): Email of the student.
            squad (str): Squad assignment.
            phonenumber (str): Phone number.
            instructor (Instructor): Assigned instructor.
        '''
        super().__init__(dod_id, name, rank, email, squad)
        self.phonenumber = phonenumber
        self.instructor = instructor

    @property
    def dod_id(self) -> str:
        '''Gets the DoD ID.'''
        return self._dod_id

    @dod_id.setter
    def dod_id(self, new_id: str):
        '''Sets the DoD ID.'''
        self._dod_id = new_id

    @property
    def name(self) -> str:
        '''Gets the name.'''
        return self._name

    @name.setter
    def name(self, new_name: str):
        '''Sets the name.'''
        self._name = new_name

    @property
    def email(self) -> str:
        '''Gets the email.'''
        return self._email

    @email.setter
    def email(self, new_email: str):
        '''Sets the email.'''
        self._email = new_email


class Instructor(Mil):
    '''
    Represents an instructor who oversees multiple students.

    Inherits from:
        Mil

    Attributes:
        students (list): List of assigned Student objects.
    '''
    def __init__(self, dod_id: str, name: str, rank: str, email: str, squad: str, students=None):
        '''
        Initializes an Instructor object.

        Args:
            dod_id (str): DoD ID.
            name (str): Name of the instructor.
            rank (str): Rank of the instructor.
            email (str): Email of the instructor.
            squad (str): Squad assignment.
            students (list, optional): List of students. Defaults to empty list.
        '''
        super().__init__(dod_id, name, rank, email, squad)
        self.students = students if students is not None else []

    @property
    def dod_id(self) -> str:
        '''Gets the DoD ID.'''
        return self._dod_id

    @dod_id.setter
    def dod_id(self, new_id: str):
        '''Sets the DoD ID.'''
        self._dod_id = new_id

    @property
    def name(self) -> str:
        '''Gets the name.'''
        return self._name

    @name.setter
    def name(self, new_name: str):
        '''Sets the name.'''
        self._name = new_name

    @property
    def email(self) -> str:
        '''Gets the email.'''
        return self._email

    @email.setter
    def email(self, new_email: str):
        '''Sets the email.'''
        self._email = new_email

    def add_stu(self, stu):
        '''
        Adds a student to the instructor’s list if not already present.

        Args:
            stu (Student): Student to add.
        '''
        if stu not in self.students:
            self.students.append(stu)

    def remove_stu(self, stu):
        '''
        Removes a student from the instructor’s list if present.

        Args:
            stu (Student): Student to remove.
        '''
        if stu in self.students:
            self.students.remove(stu)


class FortyThree92:
    '''
    Represents a 4392 request form, which may be used for leave, duty exceptions, etc.

    Attributes:
        _dod_id (str): DoD ID of the requester.
        _name (str): Full name of the requester.
        _email (str): Email of the requester.
        rank (str): Rank of the requester.
        phonenumber (str): Contact phone number.
        room (str): Room number.
        transportation (str): Type of transportation used.
        departure_date (str): Date of departure.
        arrival_one (str): First arrival date and time.
        lor_one (str): First LOR identifier.
        mileage_one (int): Mileage for the first trip.
        date_two (str): Second date (e.g., return date).
        lor_two (str): Second LOR identifier.
        other_name (str): Name of other person associated.
        address (str): Address of destination.
        other_number (str): Phone number of the other person.
        confirmation_number (str): Confirmation number for lodging.
        lodging_type (str): Type of lodging.
        visitor1_name (str): Name of the first visitor.
        visitor1_number (str): Phone number of the first visitor.
        visitor1_relationship (str): Relationship of visitor 1.
        visitor2_name (str): Name of the second visitor.
        visitor2_number (str): Phone number of the second visitor.
        visitor2_relationship (str): Relationship of visitor 2.
        status (str): Current status of the form.
    '''
    def __init__(
        self, dod_id: str, name: str, rank: str, email: str, phonenumber: str,
        room: str, transportation: str, departure_date: str, arrival_one: str,
        lor_one: str, mileage_one: int, date_two: str, lor_two: str,
        other_name: str, address: str, other_number: str,
        confirmation_number: str, lodging_type: str,
        visitor1_name: str, visitor1_number: str, visitor1_relationship: str,
        visitor2_name: str, visitor2_number: str, visitor2_relationship: str
    ):
        self._dod_id = dod_id
        self._name = name
        self._email = email
        self.rank = rank
        self.phonenumber = phonenumber
        self.room = room
        self.transportation = transportation
        self.departure_date = departure_date
        self.arrival_one = arrival_one
        self.lor_one = lor_one
        self.mileage_one = mileage_one
        self.date_two = date_two
        self.lor_two = lor_two
        self.other_name = other_name
        self.address = address
        self.other_number = other_number
        self.confirmation_number = confirmation_number
        self.lodging_type = lodging_type
        self.visitor1_name = visitor1_name
        self.visitor1_number = visitor1_number
        self.visitor1_relationship = visitor1_relationship
        self.visitor2_name = visitor2_name
        self.visitor2_number = visitor2_number
        self.visitor2_relationship = visitor2_relationship
        self.status = "Pending"

    @property
    def dod_id(self) -> str:
        '''Gets the DoD ID.'''
        return self._dod_id

    @dod_id.setter
    def dod_id(self, new_id: str):
        '''Sets the DoD ID.'''
        self._dod_id = new_id

    @property
    def name(self) -> str:
        '''Gets the name.'''
        return self._name

    @name.setter
    def name(self, new_name: str):
        '''Sets the name.'''
        self._name = new_name

    @property
    def email(self) -> str:
        '''Gets the email.'''
        return self._email

    @email.setter
    def email(self, new_email: str):
        '''Sets the email.'''
        self._email = new_email

    def get_status(self):
        pass

    def approve(self):
        pass

    def deny(self):
        pass

    def view(self):
        pass

    def cancel(self):
        pass

    def edit(self):
        pass
 