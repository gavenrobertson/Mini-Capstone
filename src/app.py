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

    def __str__(self):
        return (f"MIL: This is the base mil object.\n")


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

    def __str__(self):
        return (f"MTL:\n"
                f"  DOD ID: {self.dod_id}\n"
                f"  Name: {self.name}\n"
                f"  Rank: {self.rank}\n"
                f"  Email: {self.email}\n"
                f"  Room: {self.squad}")


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

    def __str__(self):
        return (
            f"Student:\n"
            f"  DOD ID: {self.dod_id}\n"
            f"  Name: {self.name}\n"
            f"  Rank: {self.rank}\n"
            f"  Email: {self.email}\n"
            f"  Squad: {self.squad}\n"
            f"  Phone: {self.phonenumber}\n"
            f"  Instructor: {self.instructor}"
        )


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

    def __str__(self):
        return (f"Instructor:\n"
                f"  DOD ID: {self.dod_id}\n"
                f"  Name: {self.name}\n"
                f"  Rank: {self.rank}\n"
                f"  Email: {self.email}\n"
                f"  Room: {self.squad}\n"
                f"  Subjects: {self.students}")


class FortyThree92:
    """
    Represents a 4392 request form used for leave.

    Attributes:
        name (str): Last name, First name of the student.
        phonenumber (str): Contact phone number.
        room (str): Dorm or room number.
        transportation (str): Mode of transportation.
        departure_date (str): Departure date from location.
        arrival_one (str): First arrival point.
        lor_one (str): First LOR (Length of Rest).
        mileage_one (str): Mileage for the first trip.
        date_two (str): Second date (e.g., return date).
        lor_two (str): Second LOR.
        other_name (str): Name associated with lodging.
        address (str): Lodging address.
        other_number (str): Phone number for lodging contact.
        confirmation_number (str): Lodging confirmation number.
        lodging_type (str): Type of lodging (e.g., hotel, residence).
        visitor1_name (str): Name of first approved visitor.
        visitor1_number (str): Phone number of first visitor.
        visitor1_relationship (str): Relationship of first visitor.
        visitor2_name (str): Name of second approved visitor.
        visitor2_number (str): Phone number of second visitor.
        visitor2_relationship (str): Relationship of second visitor.
        student_signature (str): Student's digital or typed signature.
        grade (str): Student's grade (E1–E4).
        date_briefed (str): Date student was briefed.
        briefed_by (str): Name of the person who briefed the student.
        status (str): Status of the form (default is "Pending").
    """
    def __init__(
        self, name, phonenumber, room, transportation,
        departure_date, arrival_one, lor_one, mileage_one,
        date_two, lor_two, other_name, address, other_number,
        confirmation_number, lodging_type,
        visitor1_name, visitor1_number, visitor1_relationship,
        visitor2_name, visitor2_number, visitor2_relationship,
        student_signature, grade, date_briefed, briefed_by
    ):
        self.name = name
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
        self.student_signature = student_signature
        self.grade = grade
        self.date_briefed = date_briefed
        self.briefed_by = briefed_by
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