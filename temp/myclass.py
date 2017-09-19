import sys
print sys.executable
print sys.version


class Employee(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


for num in [1]:
    print num

emp1 = Employee("nick", "feller")
print emp1.email


emp2 = Employee("John", "Ham")
print emp2.fullname

# cmd shift k : brings up run options
# cmd shift p : brings up all packages
