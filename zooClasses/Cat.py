from Animal import Animal


class Cat(Animal):
    breed = ''
    def __init__(self,name,breed):
        super().__init__(name,'Cat')
        self.breed = breed

        def meow(self):
            print('meow...')