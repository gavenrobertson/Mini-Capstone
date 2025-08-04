class Mil:
    '''
    Docstring
    '''
    def __init__(self, _dod_id, name, rank, email, squad):
        self._dod_id = _dod_id
        self.name = name
        self.rank = rank
        self.email = email
        self.squad = squad

    #getter
    @property
    def name(self):
        return self._name

    #setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, new_rank):
        self._rank = new_rank

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def squad(self):
        return self._squad

    @squad.setter
    def squad(self, new_squad):
        self._squad = new_squad
        

class Mtl(Mil):
    '''
    Docstring
    '''
    def __init__(self, _dod_id, name, rank, email, squad):
        super().__init__(_dod_id, name, rank, email, squad)
        
    #getter
    @property
    def name(self):
        return self._name

    #setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, new_rank):
        self._rank = new_rank

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def squad(self):
        return self._squad

    @squad.setter
    def squad(self, new_squad):
        self._squad = new_squad
    

class Student(Mil):
    '''
    Docstring
    '''
    def __init__(self, _dod_id, name, rank, email, squad, phonenumber, instructor):
        super().__init__(_dod_id, name, rank, email, squad)
        self.phonenumber = phonenumber
        self.instructor = instructor

    #getter
    @property
    def name(self):
        return self._name

    #setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, new_rank):
        self._rank = new_rank

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def squad(self):
        return self._squad

    @squad.setter
    def squad(self, new_squad):
        self._squad = new_squad

class Instrcutor(Mil):
    def __init__(self, _dod_id, name, rank, email, squad, students = None):
        super().__init__(_dod_id, name, rank, email, squad)
        if students is None:
            students = []
        else:
            self.students = students

    def add_stu(self, stu):
        if stu not in self.students:
            self.students.append(stu)

    def remove_stu(self, stu):
        if stu in self.students:
            self.students.remove(stu)

# class FortyThree92():
#     '''
#     Docstring
#     '''
#     def __init__(self, _dod_id, name, rank, email, phonenumber, squad):
        

#     def get_status(self):
#         pass

#     def approve(self):
#         pass

#     def deny(self):
#         pass

#     def view(self):
#         pass

#     def cancel(self):
#         pass

#     def edit(self):
#         pass
