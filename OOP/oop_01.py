# Object-Oriented Programming

class Application:
    
    def __init__(self, name, lastname):
        self.name = name

        self.lastname = lastname

        self.email = name + lastname + '@mail.com'
    
    def full_name(self):
        return self.name.title() + ' ' + self.lastname.title()

app_01 = Application(str(input()), input())

print(f'{app_01.name}.{app_01.lastname}@mail.com')

print(app_01.full_name())
