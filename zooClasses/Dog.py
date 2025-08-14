from Animal import Animal

class Dog(Animal):
    breed = ''
    def __init__(self,name, breed):
        super().__init__(name,'Dog')
        self.breed = breed

        def bark(self):
            print('Woof Woof...')