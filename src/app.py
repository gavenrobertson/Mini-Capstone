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
        _name (str): Name of the requester.
        _email (str): Email of the requester.
        rank (str): Rank of the requester.
        phonenumber (str): Contact phone number.
        squad (str): Squad assignment.
        status (str): Current status of the form.
    '''
    def __init__(self, dod_id: str, name: str, rank: str, email: str, phonenumber: str, squad: str):
        '''
        Initializes a FortyThree92 request form.

        Args:
            dod_id (str): DoD ID.
            name (str): Requester's name.
            rank (str): Requester's rank.
            email (str): Requester's email.
            phonenumber (str): Requester's phone number.
            squad (str): Requester's squad.
        '''
        self._dod_id = dod_id
        self._name = name
        self.rank = rank
        self._email = email
        self.phonenumber = phonenumber
        self.squad = squad
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
 