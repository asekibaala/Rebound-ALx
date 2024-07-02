class Person:
    def __init__(self, name):
        self.ame = name

    def say_hi(self):
        print('Hello, my name is', self.ame)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()