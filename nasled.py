class Human:

    head = True

    # def __init__(self):
    #     self.about()

    def say_hello(self, text):
        print(f'Здравствуйте, {text}')

class Student(Human):

    head = False

    def about(self):
        print('Я студент')

class Teacher(Human):

   pass

# human = Human()
student = Student()
teacher = Teacher()
student.say_hello('учитель')
teacher.say_hello('студент')

