from datetime import date, datetime


class Person:
    def __init__(self, name, date_birth, profession):
        self.name = name
        self._date_birth = datetime.strptime(date_birth, '%Y-%m-%d').date()
        self._profession = profession

    def __str__(self):
        return f'Name: {self.name} |Age: {self.age} |Birthday: {self._date_birth}'

    @property
    def age(self):
        return (date.today() - self._date_birth).days // 365

    def congratulates_if_birthday(self):
        today = date.today()
        print(f'Today is {today}')
        if self._date_birth.month == today.month and self._date_birth.day == today.day:
            print(f'Happy {self.age}th birthday!')
        else:
            print(f'Today is not your birthday')

    def create_profession_greeting(self):
        if self._profession:
            return f'Welcome, {self.name}. We are happy to have {self._profession} on our team'
        else:
            return f"Hello, {self.name}"


person1 = Person('Apollo', '2023-02-20', 'Data Engineer')
print('---------------------')
print('person1')
print(person1)
print('---------------------')
person1.congratulates_if_birthday()
print('---------------------')
print('person1 after increment age')
print(person1)
print('---------------------')
