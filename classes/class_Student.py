class Student():
    def __init__(self, name, age, gpa):
        '''Initializes Student class with attributes'''
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        '''Prints the object as a string'''
        return 'The student {} (age {}) has a GPA {}.'.format(self.name, self.age, self.gpa)

    def __lt__(self, other):
        '''Compares two students by GPA and returns the lowest'''
        a = self.gpa
        b = other.gpa

        if a < b:
            return '{} has the lower GPA at {} compared with {}, {}'.format(self.name, a, other.name, b)
        elif b < a:
            return '{} has the lower GPA at {} compared with {}, {}'.format(other.name, b, self.name, a)
        else:
            if a.__eq__(b):
                return '{} and {} are the same.'.format(self.name, other.name)

    def __eq__(self, other):
        '''Compares two students by name and age to determine if same'''
        a = self
        b = other
        if a.name == b.name:
            if a.age == b.age:
                if a.gpa == b.gpa:
                    return '{} and {} are the same (name, age, gpa).'.format(a.name, b.name)
                else:
                    return '{} and {} are not the same (different gpa).'.format(a.name, b.name)
            else:
                return '{} and {} are not the same (different age).'.format(a.name, b.name)
        else:
            return '{} and {} are not the same (different name).'.format(a.name, b.name)

    def __hash__(self):
        '''Computes hash of object using __key method to call attributes'''
        return hash(self.__key__())

    def __key__(self):
        '''Computes key based on object attributes'''
        return (self.name, self.age, self.gpa)
