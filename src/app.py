class Mil:
    '''
    Represents a generic military personnel.

    Attributes:
        _dod_id (str): Department of Defense ID.
        name (str): Full name of the personnel.
        rank (str): Military rank.
        email (str): Email address.
        squad (str): Assigned squad.
    '''
    def __init__(self, _dod_id: str, name: str, rank: str, email: str, squad: str):
        '''
        Initializes a Mil object.

        Args:
            _dod_id (str): DoD ID.
            name (str): Name of the personnel.
            rank (str): Rank of the personnel.
            email (str): Email of the personnel.
            squad (str): Squad assignment.
        '''
        self._dod_id = _dod_id
        self.name = name
        self.rank = rank
        self.email = email
        self.squad = squad

    @property
    def name(self) -> str:
        '''Gets the name.'''
        return self._name

    @name.setter
    def name(self, new_name: str):
        '''Sets the name.

        Args:
            new_name (str): New name to assign.
        '''
        self._name = new_name

    @property
    def rank(self) -> str:
        '''Gets the rank.'''
        return self._rank

    @rank.setter
    def rank(self, new_rank: str):
        '''Sets the rank.

        Args:
            new_rank (str): New rank to assign.
        '''
        self._rank = new_rank

    @property
    def email(self) -> str:
        '''Gets the email.'''
        return self._email

    @email.setter
    def email(self, new_email: str):
        '''Sets the email.

        Args:
            new_email (str): New email to assign.
        '''
        self._email = new_email

    @property
    def squad(self) -> str:
        '''Gets the squad.'''
        return self._squad

    @squad.setter
    def squad(self, new_squad: str):
        '''Sets the squad.

        Args:
            new_squad (str): New squad to assign.
        '''
        self._squad = new_squad


class Mtl(Mil):
    '''
    Represents a Military Training Leader (MTL).

    Inherits from:
        Mil
    '''
    def __init__(self, _dod_id: str, name: str, rank: str, email: str, squad: str):
        '''
        Initializes an MTL object.

        Args:
            _dod_id (str): DoD ID.
            name (str): Name of the MTL.
            rank (str): Rank of the MTL.
            email (str): Email of the MTL.
            squad (str): Assigned squad.
        '''
        super().__init__(_dod_id, name, rank, email, squad)


class Student(Mil):
    '''
    Represents a student under military instruction.

    Inherits from:
        Mil

    Attributes:
        phonenumber (str): Contact phone number.
        instructor (Instrcutor): Assigned instructor object.
    '''
    def __init__(self, _dod_id: str, name: str, rank: str, email: str, squad: str, phonenumber: str, instructor):
        '''
        Initializes a Student object.

        Args:
            _dod_id (str): DoD ID.
            name (str): Name of the student.
            rank (str): Rank of the student.
            email (str): Email of the student.
            squad (str): Squad assignment.
            phonenumber (str): Phone number.
            instructor (Instrcutor): Assigned instructor.
        '''
        super().__init__(_dod_id, name, rank, email, squad)
        self.phonenumber = phonenumber
        self.instructor = instructor


class Instrcutor(Mil):
    '''
    Represents an instructor who oversees multiple students.

    Inherits from:
        Mil

    Attributes:
        students (list): List of assigned Student objects.
    '''
    def __init__(self, _dod_id: str, name: str, rank: str, email: str, squad: str,
                 students=None):
        '''
        Initializes an Instructor object.

        Args:
            _dod_id (str): DoD ID.
            name (str): Name of the instructor.
            rank (str): Rank of the instructor.
            email (str): Email of the instructor.
            squad (str): Squad assignment.
            students (list, optional): List of students. Defaults to empty list.
        '''
        super().__init__(_dod_id, name, rank, email, squad)
        if students is None:
            students = []
        self.students = students

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
        name (str): Name of the requester.
        rank (str): Rank of the requester.
        email (str): Email of the requester.
        phonenumber (str): Contact phone number.
        squad (str): Squad assignment.
        status (str): Current status of the form.
    '''
    def __init__(self, _dod_id: str, name: str, rank: str, email: str,
                 phonenumber: str, squad: str):
        '''
        Initializes a FortyThree92 request form.

        Args:
            _dod_id (str): DoD ID.
            name (str): Requester's name.
            rank (str): Requester's rank.
            email (str): Requester's email.
            phonenumber (str): Requester's phone number.
            squad (str): Requester's squad.
        '''

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
